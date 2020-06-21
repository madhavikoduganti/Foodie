
 
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

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "price": "mt700", "location": "Vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "mt700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - slot{"location": "Vijayawada"}
    - slot{"cuisine": "mexican"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhu.kodu@yahoo.com"}
    - slot{"contact_email": "madhu.kodu@yahoo.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "sindian", "price": "lt300"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - form: restaurant_form
    - slot{"location": "Vadodara"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vadodara"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "maddykoduganti@gmail.com"}
    - slot{"contact_email": "maddykoduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "Vijayawada", "price": "300to700"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "300to700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "300to700"}
    - slot{"location": "Vijayawada"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Delhi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - form: restaurant_form
    - slot{"location": "Coimbatore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Jamshepur"}
    - slot{"location": "Jamshepur"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "jamshedpur"}
    - slot{"location": "jamshedpur"}
    - form: restaurant_form
    - slot{"location": "jamshedpur"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "americano"}
    - slot{"cuisine": "americano"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "jamshedpur"}
    - slot{"cuisine": "american"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"price": "mt700"}
    - slot{"price": "mt700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"price": "mt700"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - form: restaurant_form
    - action_listen
    - slot{"location": "Solapur"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search
* form: restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - restaurant_form
    - slot{"cuisine": "american"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "american"}
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
