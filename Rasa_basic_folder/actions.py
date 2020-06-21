from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_core_sdk.events import Restarted
import zomatopy
import send_mail
import json
import pandas as pd
import re
import traceback
 

import logging
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class Validator:

    def validateAndGetCuisine(self, cuisine):
        cuisine_abbrv = {"nindian":"North Indian", "sindian":"South Indian","american":"American","mexican":"Mexican", "chinese":"Chinese", "italian":"Italian"}
        if cuisine.lower() in cuisine_abbrv:
            cuisine_name = cuisine_abbrv[cuisine.lower()]
        else:
            cuisine_name = cuisine
        return cuisine_name
        

class ActionSearchRestaurants(Action):

    validator=None

    def name(self):
        return 'action_search_restaurants'

        
    def __init__(self):
          self.validator = Validator()
          super(Action, self).__init__()
          
    def run(self, dispatcher, tracker, domain):
        try:
            cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
            config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
            price_abbrv = {"lt300":"less than 300", "300to700":"in range 300 and 700","mt700":"more than 700"}
            zomato = zomatopy.initialize_app(config)
            

            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            prc = tracker.get_slot('price')

            if(cuisine is None or prc is None or loc is None):
                return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc)]

            cuisine_name = self.validator.validateAndGetCuisine(cuisine)
            loc = loc.rstrip().lower()
                
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine_name.lower())),50)
            d = json.loads(results)
            rest_name_list = []
            rest_location_list = []
            rest_rating_list = []
            rest_price_list = []
            if d['results_found'] == 0:
                dispatcher.utter_message("No Results")
            else:
                rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
                rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
                rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
                rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
                pd.set_option('display.max_colwidth', None)
                rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
                if "300" in prc and "700" in prc:
                    rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
                elif "300" in prc:
                    rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
                else:
                    rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
                rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
                dispatcher.utter_message("-----Here are the top " + cuisine_name + " restaurants in " + loc + " with avg. budget of " + price_abbrv[prc] + " Rs. for 2 people-----")
                for row in rest_df_sorted.head(5).iterrows():
                    dispatcher.utter_message(row[1]['name']+" in "+row[1]['location']+" has been rated "+row[1]['rating']+"\n")
            return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc)]
        except Exception as error:
            logger.exception(error)
            dispatcher.utter_message("Sorry! there was an error on our side. Try again later.")
            return [Restarted()]



class ActionSendEmail(Action):

    validator=None

    def name(self):
        return 'action_send_mail'
        
    def __init__(self):
          self.validator = Validator()
          super(Action, self).__init__()
          

    def run(self, dispatcher, tracker, domain):
        try:

            config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
            price_abbrv = {"lt300":"less than 300", "300to700":"in range 300 and 700","mt700":"more than 700"}
            cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
            zomato = zomatopy.initialize_app(config)
            

            loc = tracker.get_slot('location')
            prc = tracker.get_slot('price')
            cuisine = tracker.get_slot('cuisine')
            emailid = tracker.get_slot('contact_email')
            
            if(cuisine is None or prc is None or loc is None or emailid is None):
                return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc),SlotSet('contact_email',emailid)]

            cuisine_name = self.validator.validateAndGetCuisine(cuisine)
            loc = loc.rstrip().lower()
            
            
                
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine_name.lower())),50)
            d = json.loads(results)
            rest_name_list = []
            rest_location_list = []
            rest_rating_list = []
            rest_price_list = []
            if d['results_found'] == 0:
                dispatcher.utter_message("No Results")
            else:
                rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
                rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
                rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
                rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
                pd.set_option('display.max_colwidth', None)
                rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
                if "300" in prc and "700" in prc:
                   rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
                elif "300" in prc:
                   rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
                else:
                   rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]

                rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
                rest_df_html = rest_df_sorted.head(10).to_html(index=False)
                html_msg = "<p>Hi!<br>Here are the top %s restaurants in %s for budget of %s<br><br>"%(cuisine_name,loc,price_abbrv[prc.lower()])+rest_df_html+"</p>"
                try:
                    send_mail.mail_results(emailid, html_msg)
                except Exception as error1:
                    logger.exception(error1)
                    dispatcher.utter_message("Sorry! there was an error on our side. Please do check if the email provided is correct and try again.")
                    return [Restarted()]
        except Exception as error:
            logger.exception(error)
            dispatcher.utter_message("Sorry! there was an error on our side. Try again later.")
            return [Restarted()]

            

        

class ActionRestartChatHelper(Action):
    def name(self):
        return 'action_restart_chat_helper'
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]




class RestaurantForm(FormAction):
    city_list = []
    city_set = {}

    def __init__(self):
        my_file = open("CityList.txt", "r")
        self.city_list = [line.rstrip('\n').lower() for line in my_file]
        for city in self.city_list:
            self.city_set[city.lower()] = set([ch for ch in city.lower()] )
        super(FormAction, self).__init__()


    def name(self) -> Text:
        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location", "cuisine", "price"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cuisine": self.from_entity(entity="cuisine", intent="restaurant_search"),
            "location": self.from_entity(entity="location", intent="restaurant_search"),
            "price": self.from_entity(entity="price", intent=["price_info", "request_restaurant"]),
        }

    @staticmethod
    def cuisine_db() -> List[Text]:
        return [
            "chinese",
            "sindian",
            "american",
            "nindian",
            "italian",
            "mexican",
        ]
        
    @staticmethod
    def price_db() -> List[Text]:
        return [
            "lt300",
            "300to700",
            "mt700"
        ]


    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            dispatcher.utter_message("Cuisine Validated: "+value)
            return {"cuisine": value.lower()}
        else:
            dispatcher.utter_message(template="utter_wrong_cuisine")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cuisine": None}

    def validate_price(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.lower() in self.price_db():
            dispatcher.utter_message("Price Validated: "+value.lower())
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"price": value.lower()}
        else:
            dispatcher.utter_message(template="utter_wrong_price")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"price": None}


    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value is not None:
            loc = value.lstrip().rstrip().lower()
            if loc not in self.city_list:
                print(loc," not found in city_list")
                nearest_cities = self.fetch_nearest_cities(loc.lower())
                if not nearest_cities:
                    message = "We do not operate in location:"
                    message = message+str(loc)
                    message = message+" yet. Sorry!"
                    dispatcher.utter_message(template="utter_wrong_location")
                    return {"location": None}
                else:
                    message = "We do not operate in location:"
                    message = message+str(loc)
                    message = message+" yet. But, did you mean any of the following?"
                    for nearest_city in nearest_cities:
                        message += " "
                        message += nearest_city
                    dispatcher.utter_message(message)
                    return {"location": None}
            dispatcher.utter_message("Location Validated: "+value.lower())
            return {"location": value.lower()}
        else:
            dispatcher.utter_message(template="utter_wrong_location")
            return {"location": None}
            


    def fetch_nearest_cities(self, location, n=1):
        possible_city_suggestions = []
        location_set = set([ch for ch in location.lower()])
        for city in self.city_set:
            possible_city_set = self.city_set[city]
            if len(location_set.difference(possible_city_set)) <= n and len(possible_city_set.difference(location_set)) <= n:
                possible_city_suggestions.append(city)
        print("for city:",location," "," possible suggestions:", possible_city_suggestions)
        return possible_city_suggestions
            


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")
        return []
