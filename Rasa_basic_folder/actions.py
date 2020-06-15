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

class ActionSearchRestaurants(Action):
    city_list = []
    
    def __init__(self):
        my_file = open("CityList.txt", "r")
        self.city_list = [line.rstrip('\n').lower() for line in my_file]
        super(ActionSearchRestaurants, self).__init__()
        
    def name(self):
        return 'action_search_restaurants'
    
    

    def run(self, dispatcher, tracker, domain):
        try:
            cuisine_abbrv = {"nindian":"North Indian", "sindian":"South Indian","american":"American","mexican":"Mexican", "chinese":"Chinese", "italian":"Italian"}
            config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
            price_abbrv = {"LT300":"less than 300", "300To700":"in range 300 and 700","MT700":"more than 700"}
            zomato = zomatopy.initialize_app(config)
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            cuisine_name = Validator().validateAndGetCuisine(tracker.get_slot('cuisine'))
            prc = tracker.get_slot('price')
            loc = loc.lstrip().rstrip().lower()
            if loc not in self.city_list:
                print(loc," not found in city_list")
                message = "We do not operate in location:"
                message = message+str(loc)
                message = message+" yet. Sorry!"
                dispatcher.utter_message(message)
                return [Restarted()]
                
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
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
                pd.set_option('display.max_colwidth', -1)
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

class Validator:
    def validateAndGetCuisine(self, cuisine):
        cuisine_abbrv = {"nindian":"North Indian", "sindian":"South Indian","american":"American","mexican":"Mexican", "chinese":"Chinese", "italian":"Italian"}
        if cuisine.lower() in cuisine_abbrv:
            cuisine_name = cuisine_abbrv[cuisine.lower()]
        else:
            cuisine_name = cuisine
        return cuisine_name


class ActionSendEmail(Action):
    city_list = []
    
    def __init__(self):
        my_file = open("CityList.txt", "r")
        self.city_list = [line.rstrip('\n').lower() for line in my_file]
        super(ActionSendEmail, self).__init__()
        
    def name(self):
        return 'action_send_mail'
    



    def run(self, dispatcher, tracker, domain):
        try:
            config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
            price_abbrv = {"LT300":"less than 300", "300To700":"in range 300 and 700","MT700":"more than 700"}
            zomato = zomatopy.initialize_app(config)
            loc = tracker.get_slot('location')
            cuisine_name = Validator().validateAndGetCuisine(tracker.get_slot('cuisine'))
            prc = tracker.get_slot('price')
            emailid = tracker.get_slot('contact_email')
            loc = loc.lstrip().rstrip().lower()
            if loc not in self.city_list:
                print(loc," not found in city_list")
                message = "We do not operate in location:"
                message = message+str(loc)
                message = message+" yet. Sorry!"
                dispatcher.utter_message(message)
                return [Restarted()]
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
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
                pd.set_option('display.max_colwidth', -1)
                rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
                if "300" in prc and "700" in prc:
                   rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
                elif "300" in prc:
                   rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
                else:
                   rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]

                rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
                rest_df_html = rest_df_sorted.head(10).to_html(index=False)
                html_msg = "<p>Hi!<br>Here are the top %s restaurants in %s for budget of %s<br><br>"%(cuisine_name,loc,price_abbrv[prc])+rest_df_html+"</p>"
                try:
                    send_mail.mail_results(emailid, html_msg)
                except Exception as error1:
                    logger.exception(error1)
                    dispatcher.utter_message("Sorry! there was an error on our side. Please do check if the email provided is correct.")
        except Exception as error:
            logger.exception(error)
            dispatcher.utter_message("Sorry! there was an error on our side. Try again later.")

            

        

class ActionRestartChatHelper(Action):
    def name(self):
        return 'action_restart_chat_helper'
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]


