
 
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
* deny
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
* deny
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
* deny
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
* deny
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
    - slot{"location": "Solapur"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "cuisine"}
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

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "Chennai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Chennai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chennai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chennai"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "price": "300to700", "location": "Vadodara"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Vadodara"}
    - slot{"price": "300to700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "vadodara"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - slot{"location": "vadodara"}
    - slot{"cuisine": "chinese"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vadodara"}
    - slot{"cuisine": "chinese"}
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
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "location"}
* stop
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "gyderbad"}
    - slot{"location": "gyderbad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "kyderbad"}
    - slot{"location": "kyderbad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "syderbad"}
    - slot{"location": "syderbad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "lyderbad"}
    - slot{"location": "lyderbad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper



## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - form: restaurant_form
    - slot{"location": "vijayawada"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - form: restaurant_form
    - slot{"price": "lt300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* out_of_context
    - utter_default
## interactive_story_2
* out_of_context
    - utter_default
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Cpimbatore"}
    - slot{"location": "Cpimbatore"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - form: restaurant_form
    - slot{"location": "coimbatore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "americanoo"}
    - slot{"cuisine": "americanoo"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "price"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "american"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* out_of_context
    - utter_default
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "nindian", "price": "mt700", "location": "Hyderabad"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "mt700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "nindian"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* out_of_context
    - utter_default
    - utter_ask_send_details
* out_of_context
    - utter_default
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
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - restaurant_form
    - slot{"location": "vijayawada"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Visakhapatnam"}
    - slot{"location": "Visakhapatnam"}
    - form: restaurant_form
    - slot{"location": "visakhapatnam"}
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
    - slot{"location": "visakhapatnam"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_1
* restaurant_search{"cuisine": "nindian", "price": "lt300", "location": "Vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "lt300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* out_of_context
    - utter_default
* out_of_context
    - utter_default
* out_of_context
    - utter_default
* restaurant_search{"cuisine": "nindian", "price": "lt300", "location": "Vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "lt300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
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
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* out_of_context
    - utter_default
* out_of_context
    - utter_default
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
* restaurant_search
    - utter_default
    - form: restaurant_form    
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - form: restaurant_form    
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
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
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}    
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}    
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - restaurant_form
    - slot{"location": "vijayawada"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "London"}
    - slot{"location": "London"}
    - restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "hyderabda"}
    - slot{"location": "hyderabda"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - form: restaurant_form
    - slot{"price": "lt300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "300to700"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - form: restaurant_form
    - slot{"location": "vijayawada"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vijaywada"}
    - slot{"location": "Vijaywada"}
    - restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - form: restaurant_form
    - slot{"location": "vijayawada"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - restaurant_form
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "price"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
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
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - form: restaurant_form
    - slot{"location": "vadodara"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "price"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vadodara"}
    - slot{"cuisine": "american"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "price": "lt300", "location": "Mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - slot{"price": "lt300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "price": "mt700", "location": "Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Delhi"}
    - slot{"price": "mt700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "mexican"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - form: restaurant_form
    - slot{"location": "coimbatore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - form: restaurant_form
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
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
* form: restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "sydney"}
    - slot{"location": "sydney"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "sydney"}
    - slot{"location": "sydney"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper



## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "hydberad"}
    - slot{"location": "hydberad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper




## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper






## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}    
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper
    



## interactive_story_1
* restaurant_search{"location": "sydney"}
    - slot{"location": "sydney"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper


## interactive_story_1
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper




## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper



## interactive_story_1
* restaurant_search{"location": "Singapore"}
    - slot{"location": "Singapore"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper



## interactive_story_1
* restaurant_search{"location": "Rome"}
    - slot{"location": "Rome"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper





## interactive_story_1
* restaurant_search{"location": "Belgium"}
    - slot{"location": "Rome"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper






## interactive_story_1
* restaurant_search{"location": "Minsk"}
    - slot{"location": "Rome"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper







## interactive_story_1
* restaurant_search{"location": "NYC"}
    - slot{"location": "Rome"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper




## interactive_story_1
* restaurant_search{"location": "Canberra"}
    - slot{"location": "Canberra"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "pqrst"}
    - slot{"location": "pqrst"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper



## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "abcds"}
    - slot{"location": "abcds"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper




## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "vijayawafa"}
    - slot{"location": "vijayawafa"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Faridabad"}
    - slot{"location": "Faridabad"}
    - form: restaurant_form
    - slot{"location": "faridabad"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "faridabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
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
* form: restaurant_search{"location": "juridabad"}
    - slot{"location": "juridabad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "sijapur"}
    - slot{"location": "sijapur"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - form: restaurant_form
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "americano"}
    - slot{"cuisine": "americano"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "cuisine"}
* restaurant_search
    - utter_default
    - restaurant_form
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
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "american"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
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
* form: restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - form: restaurant_form
    - slot{"location": "vijayawada"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - form: restaurant_form
    - slot{"price": "mt700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "price": "lt300", "location": "bijayawad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bijayawad"}
    - slot{"price": "lt300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - slot{"location": null}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - form: restaurant_form
    - slot{"location": "vijayawada"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chennai"}
    - slot{"location": "chennai"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - form: restaurant_form
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "price"}
* price_info
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Indore"}
    - slot{"location": "Indore"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "indore"}
    - slot{"location": "indore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - form: restaurant_form
    - slot{"cuisine": "nindian"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - form: restaurant_form
    - slot{"price": "lt300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "indore"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
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
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Kakinada"}
    - slot{"location": "Kakinada"}
    - form: restaurant_form
    - slot{"location": "kakinada"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - form: restaurant_form
    - slot{"cuisine": "sindian"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "kakinada"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.clm"}
    - slot{"contact_email": "madhavi.koduganti@gmail.clm"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"price": "mt700"}
    - slot{"price": "mt700"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Finland"}
    - slot{"location": "Finland"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Vijayawafa"}
    - slot{"location": "Vijayawafa"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Cijayawada"}
    - slot{"location": "Cijayawada"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* out_of_context
    - utter_default
    - restaurant_form
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "jupiter"}
    - slot{"location": "jupiter"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "italian", "price": "300to700", "location": "Hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "300to700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "italian", "price": "lt300", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "lt300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"price": "lt300"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"price": "lt300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "nindian", "price": "300to700", "location": "Kolkata"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Kolkata"}
    - slot{"price": "300to700"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "300to700"}
    - slot{"location": "kolkata"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_2
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - form: restaurant_form
    - slot{"location": "jabalpur"}
    - slot{"requested_slot": "price"}
* form: price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - form: restaurant_form
    - slot{"price": "300to700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "jabalpur"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper
