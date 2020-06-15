from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import re

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
#import zomatopy
import json

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_range = tracker.get_slot('price')
        mail = tracker.get_slot('contact_email')
        response = "action_search_restaurants for "
        if loc is not None:
            response = response + "-----"+str(loc)
        if cuisine is not None:
            response = response + "-----"+str(cuisine)
        if price_range is not None:
            response = response +"-----"+ str(price_range)
        if mail is not None:
            response = response +"-----"+ str(mail)
        dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]



class ActionSendEmail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_range = tracker.get_slot('price')
        mail = tracker.get_slot('contact_email')
        email_lst = re.findall('\S+@\S+\.\S{2,5}', mail)
        emailId = email_lst[0]
        response = "action_send_mail for "
        if loc is not None:
            response = response + "-----"+str(loc)
        if cuisine is not None:
            response = response + "-----"+str(cuisine)
        if price_range is not None:
            response = response +"-----"+ str(price_range)
        if mail is not None:
            response = response +"-----"+ str(emailId)
        dispatcher.utter_message("-----"+response)
        return [SlotSet('contact_email',emailId)]
        
        
