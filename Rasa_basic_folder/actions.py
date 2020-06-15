from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
##import zomatopy
#import json
#from __future__ import absolute_import
#from __future__ import division
#from __future__ import unicode_literals
#
#from rasa_core.actions.action import Action
#from rasa_core.events import SlotSet
#from rasa_core.events import AllSlotsReset
import zomatopy
import send_mail
import json
import pandas as pd
import re


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
#        loc = tracker.get_slot('location')
#        cuisine = tracker.get_slot('cuisine')
#        price_range = tracker.get_slot('price')
#        mail = tracker.get_slot('contact_email')
#        response = "action_search_restaurants for "
#        if loc is not None:
#            response = response + "-----"+str(loc)
#        if cuisine is not None:
#            response = response + "-----"+str(cuisine)
#        if price_range is not None:
#            response = response +"-----"+ str(price_range)
#        if mail is not None:
#            response = response +"-----"+ str(mail)
#        dispatcher.utter_message("-----"+response)
#        return [SlotSet('location',loc)]
        config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        prc = tracker.get_slot('price')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
        print("Got cuisine:"+cuisine);
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
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
            elif prc == "300 to 700":
                rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
            else:
                rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
            rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
            dispatcher.utter_message("-----Here are the top " + cuisine + " restaurants in " + loc + " with avg. budget of " + prc + " Rs. for 2 people-----")
            for row in rest_df_sorted.head(5).iterrows():
                dispatcher.utter_message(row[1]['name']+" in "+row[1]['location']+" has been rated "+row[1]['rating']+"\n")
        return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc)]



class ActionSendEmail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
#        loc = tracker.get_slot('location')
#        cuisine = tracker.get_slot('cuisine')
#        price_range = tracker.get_slot('price')
#        mail = tracker.get_slot('contact_email')
#        email_lst = re.findall('\S+@\S+\.\S{2,5}', mail)
#        emailId = email_lst[0]
#        response = "action_send_mail for "
#        if loc is not None:
#            response = response + "-----"+str(loc)
#        if cuisine is not None:
#            response = response + "-----"+str(cuisine)
#        if price_range is not None:
#            response = response +"-----"+ str(price_range)
#        if mail is not None:
#            response = response +"-----"+ str(emailId)
#        dispatcher.utter_message("-----"+response)
#        return [SlotSet('contact_email',emailId)]
        config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        prc = tracker.get_slot('price')
        emailid = tracker.get_slot('contact_email')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
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
            if prc == "less than 300":
                rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
            elif prc == "300 to 700":
                rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
            else:
                rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
            rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
            
        rest_df_html = rest_df_sorted.head(10).to_html(index=False)
        html_msg = "<p>Hi!<br>Here are the top %s restaurants in %s for budget of %s<br><br>"%(cuisine,loc,prc)+rest_df_html+"</p>"
        send_mail.mail_results(emailid, html_msg)

        
        
