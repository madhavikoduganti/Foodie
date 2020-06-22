# Foodie
- Important settings:
-- After training with multiple stories, we have come to understand that the framework without the use of forms is rather imperfect and unreliable. Hence we decided to make use of Rasa Forms.

-- Implementations stored on GIT:
--- https://github.com/madhavikoduganti/Foodie/tree/FormIncluded - this submission
--- https://github.com/madhavikoduganti/Foodie

-- DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS = 30 
--- Default setting is 10 seconds which is very less to complete the action of sending email. The bot is not expected to run without this setting in place.
--- under Foodie/venv/lib/python3.7/site-packages/rasa/core/channels for file console.py

-- Ongoing issues with RASA:
--- https://github.com/RasaHQ/rasa/issues/4606
--- https://github.com/RasaHQ/rasa/issues/6036 - Because of this ongoing issue with RASA, you might see a few exceptions as the bot validates the slot values. Nevertheless, the dialogue flow and action sequences are well handled. 
--- Sample exceptions : 2020-06-22 18:29:34 ERROR    rasa.core.actions.action  - Failed to extract slot location with action restaurant_form





-- Sample conversations we ran with the trained bot
Your input ->  hi                                                                                                               
Hi, How can I help you!
Your input ->  please help me find some hotels                                                                                  
Where do you wanna eat?
Your input ->  in Indore                                                                                                        
? Which cuisine would you like to search for?  2: South Indian (sindian)                                                        
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  2: Rs
. 300 to 700 (300to700)                                                                                                         
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in indore with avg. budget of in range 300 and 700 Rs. for 2 people-----
Romba South in PU 13 -14, Ground Floor, Airen Heights, Opposite C21 Mall, Sector 54, Vijay Nagar, Indore has been rated 4.1
Idli Hut in Ground Floor, Vatsalya Chambers, Sapna Sangeeta, Indore has been rated 4.0
South Corner in UG 10-11, BCM Heights, PU 4, Scheme 54, Vijay Nagar, Indore has been rated 3.9
Dosa Magic in Near New Annapurna Thana, Annapurna Road, Indore has been rated 3.8
Dosa Craft in 50, Bada Sarafa, Sarafa Bazaar, Indore has been rated 3.8
Would you like for me to send the information of top 10 restaurants over an email to you?
Your input ->  yes                                                                                                              
Can you please share your email id?
Your input ->  madhavi.koduganti@gmail.com                                                                                      
Sending.... Sending... Sent you the mail :)
May our paths cross again :) Tata!!
-------END--------
Your input ->  hi                                                                                                               
Hey there! How may I help you?
Your input ->  please help me find some chinese hotels                                                                          
In which location?
Your input ->  in Pulivendla                                                                                                    
We do not operate in location:pulivendla yet. Sorry! You can either search for some other location in India or choose to stop the chat.
Where do you wanna eat?
Your input ->  stop                                                                                                             
2020-06-22 20:13:46 ERROR    rasa.core.actions.action  - Failed to extract slot location with action restaurant_form ---- >> This is a rasa ongoing issue mentioned at the start of this file
-------END--------
Your input ->  hi                                                                                                               
Hey there! How may I help you?
Your input ->   please help me find some chinese hotels                                                                         
Where would you like to eat?
Your input ->  in Rachi                                                                                                         
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  2: Rs
. 300 to 700 (300to700)                                                                                                         
Thanks. I got all the information I needed :)
-----Here are the top Chinese restaurants in ranchi with avg. budget of in range 300 and 700 Rs. for 2 people-----
Chef's Delight in 5, Main Road, Near Over Bridge, Opposite Tirath Mansion, Kanka, Ranchi has been rated 4.1
Hong  Kong in 4TH Floor, Circular Court Lalpur, Ranchi has been rated 4.0
Dumpling Momo in Shop 3, Kailash Enclave, H.B. Road, Opposite Lalpur Thana, Lalpur, Ranchi has been rated 3.7
Ni Hao in 3rd Floor, Nucleus Mall, Circular Road, Ranchi, Lalpur, Ranchi has been rated 3.4
Would you like for me to send the information of top 10 restaurants over an email to you?
Your input ->  jhaappy885@gmail.com                                                                                             
Sent. Open your mail and be amazed at my awesomeness!
Bye bye! Phir milenge chalte chalte :)
-------END--------
Your input ->  hi                                                                                                               
Hey, How is it going. How may I help you today?
Your input ->  show me some american dine outs for price less than 700                                                          
In which location?
Your input ->  in hyderabad                                                                                                     
Thanks. I got all the information I needed :)
-----Here are the top American restaurants in hyderabad with avg. budget of in range 300 and 700 Rs. for 2 people-----
GD's in HIG-A-21, APHB Colony, Jayabheri Enclave, Gachibowli, Hyderabad, Telangana 500032 has been rated 4.3
Pizza Hut in 8-2-699/2, Road 12, Amudi Nagar, Bola Nagar, Banjara Hills, Hyderabad has been rated 3.9
Pizza Hut in Ground Floor, Hyderabad Central Mall, Panjagutta, Hyderabad has been rated 3.8
Pizza Hut in Eureka Estate, Rajbhavan Road, Somajiguda, Hyderabad has been rated 3.7
Pizza Hut in Plot 67, Road 4, Chandrapuri Colony, L B Nagar, Hyderabad has been rated 3.7
Do you want this information on top 10 restaurants over an email as well?
Your input ->  no                                                                                                               
May our paths cross again :) Tata!!
-------END--------
Your input ->  hi                                                                                                               
Wassup buddy. How can I help you today?
Your input ->  show me some south eateries for price in range 300 and 700 in Bombay                                             
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in mumbai with avg. budget of in range 300 and 700 Rs. for 2 people-----
A.Rama Nayak's Udipi Shri Krishna Boarding in 1st Floor, LBS Market Building, Near Matunga Central Railway Station, Matunga East, Mumbai has been rated 4.8
Dakshinayan in Hotel Anand, Gandhigram Road, Near Hare Krishna Temple, Juhu, Mumbai has been rated 4.6
Arya Bhavan in Shop 9 & 10, Bhanujyoti Building, Opposite LBS Market, Matunga East, Mumbai has been rated 4.4
Granville IDC Kitchen in Shop 1, Bhandarkar Bhavan Court Lane, SV Road, Near Borivali Station, Borivali West, Mumbai has been rated 4.3
Dakshinayan in 183, Teen Batti Road, Walkeshwar, Malabar Hill, Mumbai has been rated 4.3
Would you like for me to send the information of top 10 restaurants over an email to you?
Your input ->  yes                                                                                                              
Can you tell me your email_id?
Your input ->  it is manasa.koduganti@gmail.com                                                                                 
Sent. Open your mail and be amazed at my awesomeness!
Bye bye! Phir milenge chalte chalte :)
-------END--------
Your input ->  hi                                                                                                               
Hey, How is it going. How may I help you today?
Your input ->  Please get me some restaurants in chennai for budget less than 700                                               
? Which cuisine would you like to search for?  2: South Indian (sindian)                                                        
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in chennai with avg. budget of in range 300 and 700 Rs. for 2 people-----
Prems Graama Bhojanam in 23/10, 3rd Main Road, Kasturba Nagar, Adyar, Chennai has been rated 4.5
That Mallu Joint in 2nd Floor, PMG Complex, GN Chetty Road, T. Nagar, Chennai has been rated 4.4
Kovai Alankar Vilas in AC 3, 2nd Avenue, Anna Nagar East, Chennai . has been rated 4.2
Nellai Vairamaligai in 60, Thirumalai Pillai Road, Rama Kamath Puram, T. Nagar, Chennai has been rated 4.2
Mana Andhra in 18/24, Khader Nawaskhan Road, Nungambakkam, Chennai has been rated 4.2
Do you want this information on top 10 restaurants over an email as well?
Your input ->  no                                                                                                               
Adios amigo!! Happy meal to you :)
-------END--------
Your input ->  show me mexican dine outs for more than 700 in Bengaluru                                                         
Thanks. I got all the information I needed :)
-----Here are the top Mexican restaurants in bangalore with avg. budget of more than 700 Rs. for 2 people-----
Windmills Craftworks in 331, EPIP Area, Near KTPO, Road 5B, Whitefield, Bangalore has been rated 4.9
Truffles in 28, 4th B Cross, Koramangala 5th Block, Bangalore has been rated 4.8
Toit in 298, 100 Feet Road, Namma Metro Pillar 62, Indiranagar, Bangalore has been rated 4.8
Chinita Real Mexican Food in 218, Near BDA Complex, Double Road, Indiranagar, Bangalore has been rated 4.5
The London Curry House - The Royale Senate Hotel in 19/3, Kumara Krupa Road, Race Course Road, Bangalore has been rated 4.5
Would you like for me to send the information of top 10 restaurants over an email to you?
Your input ->  yes                                                                                                              
can you please give me your email id?
Your input ->  maddykoduganti@gmail.com is the mail                                                                             
Sent you the mail :)
It was nice talking to you. Have a great time! :)
-------END--------
Your input ->  show me american dine outs for more than 700                                                                     
Where are you right now?
Your input ->  in Ahmedabad                                                                                                     
Thanks. I got all the information I needed :)
-----Here are the top American restaurants in ahmedabad with avg. budget of more than 700 Rs. for 2 people-----
Nini's Kitchen in 9C, Venus Atlantis, Near Shell Petrol Pump, Prahlad Nagar, Ahmedabad has been rated 4.6
Brick Kitchen - Five Petals in At Five Petals Hotel & Banquets, Near Chanakyapuri Bridge, Ghatlodia, Ahmedabad has been rated 4.4
650 - The Global Kitchen in Shreekunj Mandapam, Beside Golden Tulip Bunglows & Tulip Citadel, Rajivnagar, Ayojan Nagar has been rated 4.4
Fozzie's Pizzaiolo. Cafe. Deli in 1st Floor, Maruti Crystal, Service Road, Opposite Rajpath Club, Bodakdev, Ahmedabad has been rated 4.3
@Mango in Opposite Sindhu Bhawan, Bodakdev, Ahmedabad has been rated 4.1
Do you want this information on top 10 restaurants over an email as well?
Your input ->  no                                                                                                               
Bye-bye
-------END--------
Your input ->  show me some dine outs in mars                                                                                   
We do not operate in location:mars yet. Sorry! You can either search for some other location in India or choose to stop the chat.
Where would you like to eat?
Your input ->  stop                                                                                                             
2020-06-22 20:21:07 ERROR    rasa.core.actions.action  - Failed to extract slot location with action restaurant_form
-------END--------
Your input ->  show me some american restaurants in Canberra                                                                    
We do not operate in location:canberra yet. Sorry! You can either search for some other location in India or choose to stop the chat.
We do not operate in location:canberra yet. Sorry! You can either search for some other location in India or choose to stop the chat.
In which location?
Your input ->  in Vijayawafa                                                                                                    
We do not operate in location:vijayawafa yet. You can choose to stop or you can give any of the following valid cities. vijayawada
Where would you like to eat?
Your input ->  Vijayawada                                                                                                       
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  2: Rs
. 300 to 700 (300to700)                                                                                                         
Thanks. I got all the information I needed :)
-----Here are the top American restaurants in vijayawada with avg. budget of in range 300 and 700 Rs. for 2 people-----
KFC in Door 42/1/ 52D & 52E, MG Road, Moghalrajpuram, Labbipet, Vijayawada has been rated 4.3
KFC in 42-1-52D & 52E, Upper Ground Floor, K K Tower, D. MG Road, Acheraya Ranga Nagar, Labbipet, Vijayawada has been rated 4.2
Burger King in 3rd Floor, PVP Square Mall, MG Road, Labbipet, Vijayawada has been rated 4.2
McDonald's in Serial 132-2B, Door 59A-1-1, New P & T Colony 2, Inner Ring Road, Patamata, Vijaya, Krishna District, Auto Nagar, Vijayawada has been rated 4.2
Sweet Magic in Route 5, Besant Road, Governorpet, Vijayawada has been rated 3.9
Do you want me to email you the details of these top 10 restaurants?
Your input ->  yes to manasa.koduganti@gmail.com                                                                                
Sending.... Sending... Sent you the mail :)
It was nice talking to you. Have a great time! :)
-------END--------
Your input ->  Show me some restaurants in Minsk                                                                                
We do not operate in location:minsk yet. Sorry! You can either search for some other location in India or choose to stop the chat.
We do not operate in location:minsk yet. Sorry! You can either search for some other location in India or choose to stop the chat.
Where do you wanna eat?
Your input ->  in Mangalagiri                                                                                                   
We do not operate in location:mangalagiri yet. Sorry! You can either search for some other location in India or choose to stop the chat.
In what location?
Your input ->  in Mangalore                                                                                                     
? Which cuisine would you like to search for?  2: South Indian (sindian)                                                        
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  2: Rs
. 300 to 700 (300to700)                                                                                                         
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in mangalore with avg. budget of in range 300 and 700 Rs. for 2 people-----
Cochin Village Restaurant in D.No 17-1-28/2,17-1-28/3,17-1-28/4 Old Polie Station Kankanady Mangalore has been rated 4.4
KA-12 The Coorg Kitchenette in Ranighar, Bejai Church Cross Road, Near Bharath Gas, Bhartinagar Road Kapikad, Mangalore has been rated 4.2
Kodial Veg Restaurant in NH 66, Permannur Post, Kallapu, Mangalore has been rated 4.1
City Lunch Home in D 1-45, Iddya, Dakshina Kannada, Surathkal, Mangalore has been rated 4.0
Hotel Indrabhavana in Arya Samaj Road, Balmatta Road, Balmatta, Mangalore has been rated 3.9
Do you want me to email you the details of these top 10 restaurants?
Your input ->  no                                                                                                               
It was nice talking to you. Bye!! :)
-------END--------
Your input ->  Roses are red. Sky is blue. Upgrad is cool.                                                                      
It went over my head
Your input ->  You are idiot                                                                                                    
I could not understand
Your input ->  Anyway, I am here for finding some hotels                                                                        
Where would you like to eat?
Your input ->  in Chennai                                                                                                       
? Which cuisine would you like to search for?  Type out your own message...                                                     
Your input ->  I would like south                                                                                               
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  Type 
out your own message...                                                                                                         
Your input ->  I am damn rich. So rich that I can do way beyond 700                                                             
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in chennai with avg. budget of more than 700 Rs. for 2 people-----
Kappa Chakka Kandhari in 10, Haddows Road, Opposite Shastri Bhavan, Nungambakkam, Chennai has been rated 4.7
Southern Spice - Taj Coromandel in Taj Coromandel, 37, Mahatma Gandhi Road, Nungambakkam, Chennai has been rated 4.7
Dakshin - Crowne Plaza Chennai Adyar Park in NO.132 T T K ROAD CHENNAI ,Chennai(Tamil Nadu), -600018 has been rated 4.6
Savya Rasa in 2/10, Gandhi Mandapam Road, Kotturpuram, Chennai has been rated 4.5
Bhakshana By Paati Veedu in 2, Bagirathi Ammal Street, T. Nagar, Chennai has been rated 4.2
Do you want this information on top 10 restaurants over an email as well?
Your input ->  yes honey. Send it to jhaappy885@gmail.com                                                                       
Sent. Open your mail and be amazed at my awesomeness!
Bye buddy :)
-------END--------
Your input ->   show me some hotels in Diskit                                                                                   
We do not operate in location:diskit yet. Sorry! You can either search for some other location in India or choose to stop the chat.
We do not operate in location:diskit yet. Sorry! You can either search for some other location in India or choose to stop the chat.
In which location?
Your input ->  in Cheppai                                                                                                       
We do not operate in location:cheppai yet. You can choose to stop or you can give any of the following valid cities. chennai
In which location?
Your input ->  chennai                                                                                                          
? Which cuisine would you like to search for?  2: South Indian (sindian)                                                        
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  1: Le
sser than Rs. 300 (lt300)                                                                                                       
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in chennai with avg. budget of less than 300 Rs. for 2 people-----
Rayar's Mess in 31, Arundale Street, Mylapore, Chennai has been rated 4.6
Andhikkadai in 20, Dhandeeswaram Main Road, Velachery, Chennai has been rated 4.5
Eating Circles in 6, CP Ramaswamy Road, Alwarpet, Chennai has been rated 4.5
Murugan Idli Shop in 77-1/A, G.N. Chetty Road, T. Nagar, Chennai has been rated 4.4
Murugan Idli Shop in 149/1, 6th Avenue, Opposite Vilankanni Church, Besant Nagar, Chennai has been rated 4.3
Do you want this information on top 10 restaurants over an email as well?
Your input ->  no                                                                                                               
It was nice talking to you. Have a great time! :)
-------END--------
Your input ->  show me hotels                                                                                                   
In which location?
Your input ->  I am looking for hotels                                                                                          
I did not get it
Where do you wanna eat?
Your input ->  I wanna eat                                                                                                      
I cannot understand
Where would you like to eat?
Your input ->  I would like search for some restaurants                                                                         
I did not get it
In what location?
Your input ->  in polpata                                                                                                       
We do not operate in location:polpata yet. You can choose to stop or you can give any of the following valid cities. kolkata
Where would you like to eat?
Your input ->  in toltata                                                                                                       
We do not operate in location:toltata yet. You can choose to stop or you can give any of the following valid cities. kolkata
Where are you right now?
Your input ->  in Pilli                                                                                                         
We do not operate in location:pilli yet. Sorry! You can either search for some other location in India or choose to stop the chat.
Where are you right now?
Your input ->  in Belhi                                                                                                         
We do not operate in location:belhi yet. You can choose to stop or you can give any of the following valid cities. delhi bhilai hubli
Where would you like to eat?
Your input ->  in hubli                                                                                                         
? Which cuisine would you like to search for?  Type out your own message...                                                     
Your input ->  I would like south indian                                                                                        
? What average price range for two people are you looking at? Please mention in above ranges of <300, 300-700, >700 only.  2: Rs
. 300 to 700 (300to700)                                                                                                         
Thanks. I got all the information I needed :)
-----Here are the top South Indian restaurants in hubli with avg. budget of in range 300 and 700 Rs. for 2 people-----
Basaveshwar Khanavali in Dajiban Peth Rd, Kamaripeth, New Hubli, Hubli, Karnataka 580028 has been rated 4.5
Leelavati Palace in Opposite Urban Oasis Mall, Gokul Road, Rajendra Nagar, Hubli has been rated 4.4
Shri Renuka Restaurants in Hubli - 580020, Opposite Old KSRTC Bus Stand, New Hubli, Hubli has been rated 4.2
Do you want me to email you the details of these top 10 restaurants?
Your input ->  no                                                                                                               
Bye buddy :)
-------END--------
Your input ->   show me hotels                                                                                                  
In what location?
Your input ->    I am looking for hotels                                                                                        
I cannot understand
In which location?
Your input ->    I wanna eat                                                                                                    
I could not understand
Where are you right now?
Your input ->    I would like search for some restaurants                                                                       
It went over my head
In what location?
Your input ->    in polpata                                                                                                     
We do not operate in location:polpata yet. You can choose to stop or you can give any of the following valid cities. kolkata
In what location?
Your input ->  in bolbata                                                                                                       
We do not operate in location:bolbata yet. You can choose to stop or you can give any of the following valid cities. kolkata
In which location?
Your input ->  stop                                                                                                             
-------END--------
Your input ->     









Pip freeze:

# madhavi @ Ss-MacBook-Pro in ~/Documents/Upgrad/NLP/Asst/Foodie/Rasa_basic_folder
(venv) 
# madhavi @ Ss-MacBook-Pro in ~/Documents/Upgrad/NLP/Asst/Foodie/Rasa_basic_folder on git:FormIncluded x [20:41:25] C:130
$ pip freeze
absl-py==0.9.0
aiodns==2.0.0
aiofiles==0.5.0
aiohttp==3.6.2
alembic==1.4.2
APScheduler==3.6.3
astor==0.8.1
astunparse==1.6.3
async-generator==1.10
async-timeout==3.0.1
attrs==19.3.0
Automat==20.2.0
blinker==1.4
blis==0.4.1
boto3==1.14.2
botocore==1.17.2
cachetools==4.1.0
catalogue==1.0.0
certifi==2020.4.5.2
cffi==1.14.0
chardet==3.0.4
click==7.1.2
cloudpickle==1.3.0
colorclass==2.2.0
coloredlogs==10.0
colorhash==1.0.2
ConfigArgParse==0.13.0
constantly==15.1.0
cryptography==2.9.2
cycler==0.10.0
cymem==2.0.3
decorator==4.4.2
dnspython==1.16.0
docopt==0.6.2
docutils==0.15.2
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.2.5/en_core_web_md-2.2.5.tar.gz
fakeredis==0.10.3
fbmessenger==6.0.0
Flask==1.1.2
Flask-Cors==3.0.8
Flask-JWT-Simple==0.0.3
Flask-Mail==0.9.1
future==0.17.1
gast==0.2.2
gevent==1.5.0
gitdb==4.0.5
GitPython==3.1.3
google-auth==1.17.2
google-auth-oauthlib==0.4.1
google-pasta==0.2.0
greenlet==0.4.16
grpcio==1.29.0
h11==0.8.1
h2==3.2.0
h5py==2.10.0
hpack==3.0.0
hstspreload==2020.6.9
httplib2==0.18.1
httptools==0.1.1
httpx==0.9.3
humanfriendly==8.2
hyperframe==5.2.0
hyperlink==19.0.0
idna==2.9
importlib-metadata==1.6.1
incremental==17.5.0
isodate==0.6.0
itsdangerous==1.1.0
Jinja2==2.11.2
jmespath==0.10.0
joblib==0.15.1
jsonpickle==1.4.1
jsonschema==3.2.0
kafka-python==1.4.7
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
kiwisolver==1.2.0
klein==17.10.0
Mako==1.1.3
Markdown==3.2.2
MarkupSafe==1.1.1
matplotlib==3.2.1
mattermostwrapper==2.2
mock==4.0.2
multidict==4.7.6
murmurhash==1.0.2
networkx==2.4
numpy==1.18.5
oauth2client==4.1.3
oauthlib==3.1.0
opt-einsum==3.2.1
packaging==20.4
pandas==1.0.4
pika==1.1.0
plac==1.1.3
preshed==3.0.2
prompt-toolkit==2.0.10
protobuf==3.12.2
psycopg2-binary==2.8.5
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycares==3.1.1
pycparser==2.20
pydot==1.4.1
PyHamcrest==2.0.2
PyJWT==1.7.1
pykwalify==1.7.0
pymongo==3.8.0
pyparsing==2.4.7
pyrsistent==0.16.0
PySocks==1.7.1
python-crfsuite==0.9.7
python-dateutil==2.8.1
python-editor==1.0.4
python-engineio==3.12.1
python-socketio==4.5.1
python-telegram-bot==11.1.0
pytz==2018.9
PyYAML==5.3.1
questionary==1.5.2
rasa==1.10.3
rasa-core==0.14.5
rasa-core-sdk==0.14.0
rasa-nlu==0.15.1
rasa-sdk==1.10.1
rasa-x==0.29.1
redis==3.5.3
requests==2.23.0
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rfc3986==1.4.0
rocketchat-API==0.6.36
rsa==4.6
ruamel.yaml==0.16.10
ruamel.yaml.clib==0.2.0
s3transfer==0.3.3
sanic==19.12.2
Sanic-Cors==0.10.0.post3
sanic-jwt==1.3.2
Sanic-Plugins-Framework==0.9.2
scikit-learn==0.22.2.post1
scipy==1.4.1
simplejson==3.17.0
six==1.15.0
sklearn-crfsuite==0.3.6
slackclient==2.0.0
smmap==3.0.4
sniffio==1.1.0
spacy==2.2.4
SQLAlchemy==1.3.17
srsly==1.0.2
tabulate==0.8.7
tensorboard==2.1.1
tensorboard-plugin-wit==1.6.0.post3
tensorflow==2.1.0
tensorflow-addons==0.7.1
tensorflow-estimator==2.1.0
tensorflow-hub==0.8.0
tensorflow-probability==0.9.0
termcolor==1.1.0
terminaltables==3.1.0
thinc==7.4.0
tornado==6.0.4
tqdm==4.45.0
twilio==6.26.3
Twisted==20.3.0
typing==3.7.4.1
tzlocal==2.1
ujson==1.35
urllib3==1.25.9
uvloop==0.14.0
wasabi==0.6.0
wcwidth==0.2.4
webexteamssdk==1.3
websocket-client==0.54.0
websockets==8.1
Werkzeug==1.0.1
wrapt==1.12.1
yarl==1.4.2
zipp==3.1.0
zope.interface==5.1.0
(venv) 
# madhavi @ Ss-MacBook-Pro in ~/Documents/Upgrad/NLP/Asst/Foodie/Rasa_basic_folder on git:FormIncluded x [20:41:30] 
$ 

