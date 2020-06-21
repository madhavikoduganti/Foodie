## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Tiruchirapalli"}
    - slot{"location": "Tiruchirapalli"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Tiruchirapalli"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "johndoe@amazon.com"}
    - slot{"contact_email": "johndoe@amazon.com"}
    - action_send_mail
    - slot{"location": "Tiruchirapalli"}
    - action_validate_location
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Madurai"}
    - slot{"location": "Madurai"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "Madurai"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "nindian", "location": "Kozhikode"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Kozhikode"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "Kozhikode"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "Rishikesh"}
    - utter_ask_send_details
* contact_id{"contact_email": "xyz@sth.edu"}
    - slot{"contact_email": "xyz@sth.edu"}
    - action_send_mail
    - slot{"location": "Rishikesh"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_validate_location    
    - utter_ask_cuisine
* None{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* None{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madd@yahoo.com"}
    - slot{"contact_email": "madd@yahoo.com"}
    - action_send_mail
    - slot{"location": "Lucknow"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.kodu@yahoo.com"}
    - slot{"contact_email": "madhavi.kodu@yahoo.com"}
    - action_send_mail
    - slot{"location": "kolkata"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

 

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "sindian", "location": "Kurnool"}
    - slot{"cuisine": "sindian"}
    - slot{"location": "Kurnool"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "Kurnool"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "lt300"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Gurgaon"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Dehradun"}
    - utter_ask_send_details
* contact_id{"contact_email": "r123@ttsi.cos"}
    - slot{"contact_email": "r123@ttsi.cos"}
    - action_send_mail
    - slot{"contact_email": "r123@ttsi.cos"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "wwstei@grrr.wgo"}
    - slot{"contact_email": "wwstei@grrr.wgo"}
    - action_send_mail
    - slot{"contact_email": "wwstei@grrr.wgo"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "sindian", "price": "mt700", "location": "Kozhikode"}
    - slot{"cuisine": "sindian"}
    - slot{"location": "Kozhikode"}
    - slot{"price": "mt700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "Kozhikode"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "iieta@ttya.com"}
    - slot{"contact_email": "iieta@ttya.com"}
    - action_send_mail
    - slot{"contact_email": "iieta@ttya.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Vadodara", "price": "300to700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Vadodara"}
    - slot{"price": "300to700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "aagt@yytad.coww"}
    - slot{"contact_email": "aagt@yytad.coww"}
    - action_send_mail
    - slot{"contact_email": "aagt@yytad.coww"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Mangalore", "price": "300to700"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mangalore"}
    - slot{"price": "300to700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "Mangalore"}
    - utter_ask_send_details
* contact_id{"contact_email": "happyhappybro@wasssuupp.co"}
    - slot{"contact_email": "happyhappybro@wasssuupp.co"}
    - action_send_mail
    - slot{"contact_email": "happyhappybro@wasssuupp.co"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_send_details
* contact_id{"contact_email": "blablablew@puppyinc.com"}
    - slot{"contact_email": "blablablew@puppyinc.com"}
    - action_send_mail
    - slot{"contact_email": "blablablew@puppyinc.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "Chennai", "price": "mt700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Chennai"}
    - slot{"price": "mt700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_send_details
* contact_id{"contact_email": "witty@humour.inc"}
    - slot{"contact_email": "witty@humour.inc"}
    - action_send_mail
    - slot{"contact_email": "witty@humour.inc"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "Ghaziabad"}
    - utter_ask_send_details
* contact_id{"contact_email": "wwrtey@rediff.com"}
    - slot{"contact_email": "wwrtey@rediff.com"}
    - action_send_mail
    - slot{"contact_email": "wwrtey@rediff.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Indore"}
    - slot{"location": "Indore"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Indore"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "wwalia@upgrad.com"}
    - slot{"contact_email": "wwalia@upgrad.com"}
    - action_send_mail
    - slot{"contact_email": "wwalia@upgrad.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_ask_send_details
* contact_id{"contact_email": "vikram@twitter.com"}
    - slot{"contact_email": "vikram@twitter.com"}
    - action_send_mail
    - slot{"contact_email": "vikram@twitter.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* affirm{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_ask_send_details
* contact_id{"contact_email": "whoswho@gmail.com"}
    - slot{"contact_email": "whoswho@gmail.com"}
    - action_send_mail
    - slot{"contact_email": "whoswho@gmail.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "Aligarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Aligarh"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"contact_email": "lt300"}
    - slot{"contact_email": "lt300"}
    - action_search_restaurants
    - slot{"location": "Aligarh"}
    - utter_ask_send_details
* contact_id{"contact_email": "mkd@yahoo.co.in"}
    - slot{"contact_email": "mkd@yahoo.co.in"}
    - action_send_mail
    - slot{"contact_email": "mkd@yahoo.co.in"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "Indore"}
    - slot{"location": "Indore"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "Indore"}
    - utter_ask_send_details
* contact_id{"contact_email": "mybutler@yahoo.co.in"}
    - slot{"contact_email": "mybutler@yahoo.co.in"}
    - action_send_mail
    - slot{"contact_email": "mybutler@yahoo.co.in"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "Hyderabad"}
    - slot{"cuisine": "american"}
    - slot{"location": "Hyderabad"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "american"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
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
* restaurant_search{"location": "rreywif"}
    - slot{"location": "rreywif"}
    - action_validate_location    


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Bhilai"}
    - slot{"location": "Bhilai"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "bhilai"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
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
* restaurant_search{"location": "ggfgeurgedfg"}
    - slot{"location": "ggfgeurgedfg"}
    - action_validate_location    

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hyderabad", "price": "mt700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "mt700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
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
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Vijayawada", "price": "lt300", "cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "lt300"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Cuttack"}
    - slot{"location": "Cuttack"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "cuttack"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Guntur"}
    - slot{"location": "Guntur"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "guntur"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
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
* restaurant_search{"location": "Visakhapatnam"}
    - slot{"location": "Visakhapatnam"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "visakhapatnam"}
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
* restaurant_search{"location": "Vijayawada", "price": "lt300"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "lt300"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "Vijayawada", "price": "lt300"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "lt300"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
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
* restaurant_search{"cuisine": "nindian", "location": "chennai", "price": "mt700"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "chennai"}
    - slot{"price": "mt700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - utter_ask_location
* price_info{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet

## interactive_story_2
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
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
* restaurant_search{"cuisine": "italian", "location": "Nashik", "price": "mt700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Nashik"}
    - slot{"price": "mt700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "nashik"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "Coimbatore", "price": "mt700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Coimbatore"}
    - slot{"price": "mt700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "coimbatore"}
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
* restaurant_search{"cuisine": "italian", "location": "Bhavnagar", "price": "mt700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Bhavnagar"}
    - slot{"price": "mt700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "bhavnagar"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
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
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "moradabad"}
    - slot{"cuisine": "american"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "nindian", "price": "lt300", "location": "Bareilly"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Bareilly"}
    - slot{"price": "lt300"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "bareilly"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gibberland"}
    - slot{"location": "gibberland"}
    - action_validate_location

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "transylvania"}
    - slot{"location": "transylvania"}
    - action_validate_location


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* price_info{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "sindian", "location": "Goa", "price": "lt300"}
    - slot{"cuisine": "sindian"}
    - slot{"location": "Goa"}
    - slot{"price": "lt300"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
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
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - slot{"cuisine": "mexican"}
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

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "mt700", "location": "roURkeLa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "roURkeLa"}
    - slot{"price": "mt700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "rourkela"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "JaLaNDHaR"}
    - slot{"location": "JaLaNDHaR"}
    - action_validate_location
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "JalaNDhaR"}
    - slot{"location": "JalaNDhaR"}
    - action_validate_location
    - slot{"location": "jalandhar"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_validate_location
    - slot{"location": "moradabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "moradabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_location
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_validate_location
    - slot{"location": "solapur"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price": "300to700", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - slot{"price": "300to700"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "american"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"price": "lt300"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "american"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_validate_location
    - slot{"location": "dehradun"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - action_search_restaurants
    - slot{"location": "dehradun"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_1
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_validate_location
    - slot{"location": "ranchi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mt700"}
    - slot{"price": "mt700"}
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kozikode"}
    - slot{"location": "kozikode"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - action_validate_location
    - slot{"location": "kozhikode"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "kozhikode"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kakiada"}
    - slot{"location": "Kakiada"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "kakinada"}
    - slot{"location": "kakinada"}
    - action_validate_location
    - slot{"location": "kakinada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "kakinada"}
    - slot{"cuisine": "chinese"}
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
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bijayawada"}
    - slot{"location": "Bijayawada"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vijayawafa"}
    - slot{"location": "Vijayawafa"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper





## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "fangalore"}
    - slot{"location": "fangalore"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "sindian", "location": "poa", "price": "lt300"}
    - slot{"cuisine": "sindian"}
    - slot{"location": "Poa"}
    - slot{"price": "lt300"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
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
* restaurant_search{"location": "nurat"}
    - slot{"location": "nurat"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - slot{"cuisine": "mexican"}
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

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "mt700", "location": "roURkeLa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "poURkeLa"}
    - slot{"price": "mt700"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "roURKela"}
    - slot{"location": "roURKela"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "rourkela"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "BaLaNDHaR"}
    - slot{"location": "BaLaNDHaR"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "JaLaNDHaR"}
    - slot{"location": "JaLaNDHaR"}
    - action_validate_location
    - slot{"location": "jalandhar"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper
 

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "pijayawada", "cuisine": "chinese", "price": "lt300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pijayawada"}
    - slot{"price": "lt300"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "vijYwafa"}
    - slot{"location": "vijYwafa"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vijayawafa"}
    - slot{"location": "Vijayawafa"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "durnool"}
    - slot{"location": "durnool"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "furnool"}
    - slot{"location": "furnool"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "kurnool"}
    - slot{"location": "kurnool"}
    - action_validate_location
    - slot{"location": "kurnool"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "kurnool"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "mt700", "location": "pyderbad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pyderbad"}
    - slot{"price": "mt700"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "kyderabad"}
    - slot{"location": "kyderabad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "ryderbad"}
    - slot{"location": "ryderbad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "wyderbad"}
    - slot{"location": "wyderbad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "lyderbad"}
    - slot{"location": "lyderbad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "syderbad"}
    - slot{"location": "syderbad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "zyderabad"}
    - slot{"location": "zyderabad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "sindian", "price": "lt300", "location": "lumbai"}
    - slot{"cuisine": "sindian"}
    - slot{"location": "lumbai"}
    - slot{"price": "lt300"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_validate_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "allahabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "lt300"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Kakinada"}
    - slot{"location": "Kakinada"}
    - action_validate_location
    - slot{"location": "kakinada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "kakinada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Almedabad"}
    - slot{"location": "Almedabad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_validate_location
    - slot{"location": "ahmedabad"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Byderbad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Byderbad"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vylarabad"}
    - slot{"location": "Vylarabad"}
    - action_validate_location

## interactive_story_2
* restaurant_search{"cuisine": "chinese", "location": "Varoda"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Varoda"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "paranasi"}
    - slot{"location": "paranasi"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "tiruchirapali"}
    - slot{"location": "tiruchirapali"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "piruchirapalli"}
    - slot{"location": "piruchirapalli"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "soupkela"}
    - slot{"location": "soupkela"}
    - action_validate_location

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_validate_location
    - slot{"location": "moradabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "moradabad"}
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
    - utter_ask_location
* restaurant_search{"location": "Vellore"}
    - slot{"location": "Vellore"}
    - action_validate_location
    - slot{"location": "vellore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "vellore"}
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
* restaurant_search{"cuisine": "nindian", "price": "mt700", "location": "Bhavnagar"}
    - slot{"cuisine": "nindian"}
    - slot{"location": "Bhavnagar"}
    - slot{"price": "mt700"}
    - action_validate_location
    - slot{"location": "bhavnagar"}
    - action_search_restaurants
    - slot{"location": "bhavnagar"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_2
* restaurant_search{"cuisine": "chinese", "price": "lt300", "location": "Bhaavnaga"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhaavnaga"}
    - slot{"price": "lt300"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Bhavnagar"}
    - slot{"location": "Bhavnagar"}
    - action_validate_location
    - slot{"location": "bhavnagar"}
    - action_search_restaurants
    - slot{"location": "bhavnagar"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_2
* restaurant_search{"cuisine": "sindian", "price": "mt700", "location": "vhavnagar"}
    - slot{"cuisine": "sindian"}
    - slot{"location": "vhavnagar"}
    - slot{"price": "mt700"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "chavnagar"}
    - slot{"location": "chavnagar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "jhavnagar"}
    - slot{"location": "jhavnagar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "khavnagar"}
    - slot{"location": "khavnagar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "lhavnagar"}
    - slot{"location": "lhavnagar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "shavnagar"}
    - slot{"location": "shavnagar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "ghavnagar"}
    - slot{"location": "ghavnagar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Bhavnagar"}
    - slot{"location": "Bhavnagar"}
    - action_validate_location
    - slot{"location": "bhavnagar"}
    - action_search_restaurants
    - slot{"location": "bhavnagar"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
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
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "vijayawafa"}
    - slot{"location": "vijayawafa"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "bijayawada"}
    - slot{"location": "bijayawada"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "lijayawada"}
    - slot{"location": "lijayawada"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "zijayawada"}
    - slot{"location": "zijayawada"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "rajahmundry"}
    - slot{"location": "rajahmundry"}
    - action_validate_location
    - slot{"location": "rajahmundry"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "rajahmundry"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "price": "300to700", "location": "Hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "300to700"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
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
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "more than 300", "cuisine": "chinese", "location": "Chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chennai"}
    - slot{"price": "more than 300"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_price_range
* price_info{"price": "than 300"}
    - slot{"price": "than 300"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_price_range
* price_info
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": null}
    - utter_ask_price_range
* price_info
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": null}
    - utter_ask_price_range
* price_info
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": null}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_validate_location
    - slot{"location": "solapur"}
    - utter_ask_price_range
* price_info{"price": "than 300"}
    - slot{"price": "than 300"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "italian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

 

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_validate_location
    - slot{"location": "ranchi"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"cuisine": "chinese"}
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
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
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
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhappy885@gmail.com"}
    - slot{"contact_email": "jhappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_location
* restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_validate_location
    - slot{"location": "coimbatore"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_validate_location
    - slot{"location": "moradabad"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "moradabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Faridabad"}
    - slot{"location": "Faridabad"}
    - action_validate_location
    - slot{"location": "faridabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "faridabad"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search

## interactive_story_2
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location

## interactive_story_3
* restaurant_search{"price": "lt300"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"price": "mt700"}
    - slot{"price": "mt700"}
    - utter_ask_location
* restaurant_search{"location": "Ujjain"}
    - slot{"location": "Ujjain"}
    - action_validate_location
    - slot{"location": "ujjain"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "nindian"}
    - slot{"cuisine": "nindian"}
    - action_search_restaurants
    - slot{"location": "ujjain"}
    - slot{"cuisine": "nindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_2
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - action_validate_location
    - slot{"location": "rajkot"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - action_search_restaurants
    - slot{"location": "rajkot"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_2
* restaurant_search{"price": "mt700"}
    - slot{"price": "mt700"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_location
    - slot{"location": "patna"}
    - utter_ask_price_range
* price_info{"price": "lt300"}
    - slot{"price": "lt300"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_validate_location
    - slot{"location": "gurgaon"}
    - utter_ask_price_range
* price_info{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "sindian"}
    - slot{"cuisine": "sindian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawfa"}
    - slot{"location": "Vijayawfa"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vijayawaza"}
    - slot{"location": "Vijayawaza"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper



## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - action_validate_location
    - slot{"location": "ghaziabad"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "ghaziabad"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "price": "300to700", "location": "Bijapur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bijapur"}
    - slot{"price": "300to700"}
    - action_validate_location
    - slot{"location": "bijapur"}
    - action_search_restaurants
    - slot{"location": "bijapur"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper


## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
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
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - action_validate_location
    - slot{"location": "ghaziabad"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "ghaziabad"}
    - slot{"cuisine": "chinese"}
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
* restaurant_search{"cuisine": "mexican", "price": "mt700"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mt700"}
    - utter_ask_location
* restaurant_search{"location": "Kurnool"}
    - slot{"location": "Kurnool"}
    - action_validate_location
    - slot{"location": "kurnool"}
    - action_search_restaurants
    - slot{"location": "kurnool"}
    - slot{"cuisine": "mexican"}
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
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "300to700"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "lt300"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_validate_location
    - slot{"location": "ahmedabad"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "mexican"}
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
* restaurant_search{"cuisine": "italian", "price": "lt300"}
    - slot{"cuisine": "italian"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_validate_location
    - slot{"location": "ahmedabad"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "italian"}
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
* restaurant_search{"cuisine": "italian", "price": "mt700"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mt700"}
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_validate_location
    - slot{"location": "ahmedabad"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "italian"}
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
* restaurant_search{"cuisine": "sindian", "price": "300to700"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "sindian", "price": "300to700"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "Bhubaneswat"}
    - slot{"location": "Bhubaneswat"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - action_validate_location
    - slot{"location": "bhubaneswar"}
    - action_search_restaurants
    - slot{"location": "bhubaneswar"}
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
    - utter_ask_location
* restaurant_search{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - action_validate_location
    - slot{"location": "ghaziabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "mt700"}
    - slot{"price": "mt700"}
    - action_search_restaurants
    - slot{"location": "ghaziabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "mt700"}
    - utter_ask_send_details
* contact_id{"contact_email": "madhavi.koduganti@gmail.com"}
    - slot{"contact_email": "madhavi.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_2
* restaurant_search{"cuisine": "sindian", "price": "300to700"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_location
* restaurant_search{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - action_validate_location
    - slot{"location": "bhubaneswar"}
    - action_search_restaurants
    - slot{"location": "bhubaneswar"}
    - slot{"cuisine": "sindian"}
    - slot{"price": "300to700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "price": "lt300"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_validate_location
    - slot{"location": "solapur"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* affirm
    - utter_ask_id
* contact_id{"contact_email": "maddykoduganti@gmail.com"}
    - slot{"contact_email": "maddykoduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "price": "lt300"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_location
    - slot{"location": "patna"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper




## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "lt300"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_location
    - slot{"location": "patna"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper





## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "lt300"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "lt300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper
