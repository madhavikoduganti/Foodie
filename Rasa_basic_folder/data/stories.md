## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Tiruchirapalli"}
    - slot{"location": "Tiruchirapalli"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "Tiruchirapalli"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "johndoe@amazon.com"}
    - slot{"contact_email": "johndoe@amazon.com"}
    - action_send_mail
    - slot{"location": "Tiruchirapalli"}
    - utter_sent_mail
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "ygndgf1233@yyrt.de"}
    - slot{"contact_email": "ygndgf1233@yyrt.de"}
    - action_send_mail
    - slot{"location": "chandigarh"}
    - utter_sent_mail
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - slot{"location": "Mumbai"}
    - utter_sent_mail
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Madurai"}
    - slot{"location": "Madurai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "Madurai"}
    - utter_ask_send_details
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_send_details
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_send_details
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - slot{"location": "bengaluru"}
    - utter_sent_mail
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "NIndian", "location": "Kozhikode"}
    - slot{"cuisine": "NIndian"}
    - slot{"location": "Kozhikode"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "Kozhikode"}
    - utter_ask_send_details
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "Rishikesh"}
    - utter_ask_send_details
* contact_id{"contact_email": "xyz@sth.edu"}
    - slot{"contact_email": "xyz@sth.edu"}
    - action_send_mail
    - slot{"location": "Rishikesh"}
    - utter_sent_mail
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "manmanman@madhavi.com"}
    - slot{"contact_email": "manmanman@madhavi.com"}
    - action_send_mail
    - slot{"location": "Kolkata"}
    - utter_sent_mail
    - utter_goodbye
