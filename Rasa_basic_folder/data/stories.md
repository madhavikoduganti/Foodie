
 
## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - form: restaurant_form
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "Hyderabad"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "Hyderabad"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart_chat_helper


 

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - form: restaurant_form
    - slot{"location": "Vijayawada"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - form: restaurant_form
    - slot{"price": "lt300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - form: restaurant_form
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - form: restaurant_form
    - slot{"location": "Patna"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_validate_location
    - slot{"location": "patna"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "hyderbad"}
    - slot{"location": "hyderbad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "byderabad"}
    - slot{"location": "byderabad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "Hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - form: restaurant_form
    - slot{"cuisine": "nindian"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper
