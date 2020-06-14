from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

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
        response = "action_search_restaurants for "+loc +" "+cuisine+" "+price_range+" "+mail
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
        response = "action_send_mail for "+loc +" "+cuisine+" "+price_range+" "+mail
        dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]

