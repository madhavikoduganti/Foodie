## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Tiruchirapalli"}
    - slot{"location": "Tiruchirapalli"}
    - action_validate_location    
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "NIndian", "location": "Kozhikode"}
    - slot{"cuisine": "NIndian"}
    - slot{"location": "Kozhikode"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_validate_location    
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
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_validate_location    
    - utter_ask_cuisine
* None{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_range
* None{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "SIndian", "location": "Kurnool"}
    - slot{"cuisine": "SIndian"}
    - slot{"location": "Kurnool"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"price": "LT300"}
    - slot{"price": "LT300"}
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
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
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
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "SIndian", "price": "MT700", "location": "Kozhikode"}
    - slot{"cuisine": "SIndian"}
    - slot{"location": "Kozhikode"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "Mexican", "location": "Vadodara", "price": "300To700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Vadodara"}
    - slot{"price": "300To700"}
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
* restaurant_search{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_validate_location    
    - utter_ask_location
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_ask_send_details
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
* restaurant_search{"cuisine": "American", "location": "Mangalore", "price": "300To700"}
    - slot{"cuisine": "American"}
    - slot{"location": "Mangalore"}
    - slot{"price": "300To700"}
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
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "Mexican", "location": "Chennai", "price": "MT700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Chennai"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "Mexican", "location": "Aligarh"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Aligarh"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"contact_email": "LT300"}
    - slot{"contact_email": "LT300"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "American", "location": "Hyderabad"}
    - slot{"cuisine": "American"}
    - slot{"location": "Hyderabad"}
    - action_validate_location    
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "American"}
    - slot{"price": "300To700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "bhilai"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "Mexican", "location": "Hyderabad", "price": "MT700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "MT700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
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
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300To700"}
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
* restaurant_search{"location": "Vijayawada", "price": "LT300", "cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "LT300"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "cuttack"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "guntur"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "visakhapatnam"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "MT700"}
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
* restaurant_search{"location": "Vijayawada", "price": "LT300"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "LT300"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"location": "Vijayawada", "price": "LT300"}
    - slot{"location": "Vijayawada"}
    - slot{"price": "LT300"}
    - action_validate_location    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "NIndian", "location": "chennai", "price": "MT700"}
    - slot{"cuisine": "NIndian"}
    - slot{"location": "chennai"}
    - slot{"price": "MT700"}
    - action_validate_location    
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "Italian", "location": "Nashik", "price": "MT700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Nashik"}
    - slot{"price": "MT700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "nashik"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "Mexican", "location": "Coimbatore", "price": "MT700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Coimbatore"}
    - slot{"price": "MT700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "Italian", "location": "Bhavnagar", "price": "MT700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Bhavnagar"}
    - slot{"price": "MT700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "bhavnagar"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "moradabad"}
    - slot{"cuisine": "American"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "NIndian", "price": "LT300", "location": "Bareilly"}
    - slot{"cuisine": "NIndian"}
    - slot{"location": "Bareilly"}
    - slot{"price": "LT300"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "bareilly"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "LT300"}
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
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "MT700"}
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
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "SIndian", "location": "Goa", "price": "LT300"}
    - slot{"cuisine": "SIndian"}
    - slot{"location": "Goa"}
    - slot{"price": "LT300"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "chinese", "price": "MT700", "location": "roURkeLa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "roURkeLa"}
    - slot{"price": "MT700"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "rourkela"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "JaLaNDHaR"}
    - slot{"location": "JaLaNDHaR"}
    - action_validate_location
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "JalaNDhaR"}
    - slot{"location": "JalaNDhaR"}
    - action_validate_location
    - slot{"location": "jalandhar"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "moradabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "300To700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants

## interactive_story_2
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_validate_location
    - slot{"location": "ranchi"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300To700"}
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
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_location
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_validate_location
    - slot{"location": "solapur"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "solapur"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "NIndian"}
    - slot{"cuisine": "NIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - utter_ask_location
* restaurant_search{"location": "Madurai"}
    - slot{"location": "Madurai"}
    - action_validate_location
    - slot{"location": "madurai"}
    - action_search_restaurants
    - slot{"location": "madurai"}
    - slot{"cuisine": "NIndian"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "price": "300To700", "location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"location": "Mumbai"}
    - slot{"price": "300To700"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "American"}
    - slot{"price": "300To700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_validate_location
    - slot{"location": "vijayawada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "American"}
    - slot{"price": "LT300"}
    - utter_ask_send_details
* contact_id{"contact_email": "jhaappy885@gmail.com"}
    - slot{"contact_email": "jhaappy885@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - utter_ask_location
* greet{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_validate_location
    - slot{"location": "dehradun"}
    - utter_ask_cuisine
* greet{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - action_search_restaurants
    - slot{"location": "dehradun"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "300To700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - utter_ask_location
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_location
* out_of_scope
    - utter_ask_location
* restaurant_search{"location": "Guntur"}
    - slot{"location": "Guntur"}
    - action_validate_location
    - slot{"location": "guntur"}
    - action_search_restaurants
    - slot{"location": "guntur"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
    - utter_ask_send_details
* out_of_scope
    - utter_ask_send_details
* out_of_scope
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
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_validate_location
    - slot{"location": "ranchi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "America"}
    - slot{"cuisine": "America"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"cuisine": "America"}
    - slot{"price": "300To700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "MT700"}
    - slot{"price": "MT700"}
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
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
* affirm{"location": "kozikode"}
    - slot{"location": "kozikode"}
    - action_validate_location
    - slot{"location": null}
* affirm{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - action_validate_location
    - slot{"location": "kozhikode"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "kozhikode"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "MT700"}
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
* deny{"location": "kakinada"}
    - slot{"location": "kakinada"}
    - action_validate_location
    - slot{"location": "kakinada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "kakinada"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300To700"}
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
* restaurant_search{"cuisine": "SIndian"}
    - slot{"cuisine": "SIndian"}
    - utter_ask_price_range
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "vijayawada"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
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
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "SIndian", "location": "Goa", "price": "LT300"}
    - slot{"cuisine": "SIndian"}
    - slot{"location": "Poa"}
    - slot{"price": "LT300"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
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
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
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
* restaurant_search{"cuisine": "chinese", "price": "MT700", "location": "roURkeLa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "poURkeLa"}
    - slot{"price": "MT700"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "roURKela"}
    - slot{"location": "roURKela"}
    - action_validate_location
    - action_search_restaurants
    - slot{"location": "rourkela"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
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
* price_info{"price": "MT700"}
    - slot{"price": "MT700"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper
 

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "pijayawada", "cuisine": "chinese", "price": "LT300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pijayawada"}
    - slot{"price": "LT300"}
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
    - slot{"price": "LT300"}
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
* price_info{"price": "300To700"}
    - slot{"price": "300To700"}
    - action_search_restaurants
    - slot{"location": "kurnool"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300To700"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "price": "MT700", "location": "pyderbad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "pyderbad"}
    - slot{"price": "MT700"}
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
    - slot{"cuisine": "Mexican"}
    - slot{"price": "MT700"}
    - utter_ask_send_details
* contact_id{"contact_email": "manasa.koduganti@gmail.com"}
    - slot{"contact_email": "manasa.koduganti@gmail.com"}
    - action_send_mail
    - utter_sent_mail
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* restaurant_search{"cuisine": "SIndian", "price": "LT300", "location": "lumbai"}
    - slot{"cuisine": "SIndian"}
    - slot{"location": "lumbai"}
    - slot{"price": "LT300"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "SIndian"}
    - slot{"price": "LT300"}
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
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "allahabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "LT300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "LT300"}
    - slot{"price": "LT300"}
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
    - slot{"price": "LT300"}
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
* price_info{"price": "LT300"}
    - slot{"price": "LT300"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "LT300"}
    - utter_ask_send_details
* deny
    - utter_goodbye
    - action_restart_chat_helper

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Byderbad"}
    - slot{"cuisine": "Mexican"}
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
* deny{"location": "soupkela"}
    - slot{"location": "soupkela"}
    - action_validate_location
