## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- yay
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Thanks
- yes. please send it
- [Prayagraj]{"entity": "location", "value": "Allahabad"}

## intent:deny
- no
- not necessary
- no. that's okay
- no. that's not needed
- no. that's ok
- not needed
- nope
- nada
- no that's fine
- no that's unnecessary
- no that is unnecessary
- unnecessary
- no thanks
- no, thanks
- no. not needed
- don't send
- why? it is not necessary

## intent:price_info
- [LT300](price)
- [MT700](price)
- [300To700](price)
- [Less than Rs. 300]{"entity": "price", "value": "LT300"}
- [less than 300]{"entity": "price", "value": "LT300"}
- [Less than 300]{"entity": "price", "value": "LT300"}
- [300]{"entity": "price", "value": "LT300"}
- [<300]{"entity": "price", "value": "LT300"}
- [< 300]{"entity": "price", "value": "LT300"}
- [Lesser than Rs. 300]{"entity": "price", "value": "LT300"}
- [below 300]{"entity": "price", "value": "LT300"}
- [300-700]{"entity": "price", "value": "300To700"} range
- [between 300 and 700]{"entity": "price", "value": "300To700"}
- [Rs. 300 to 700]{"entity": "price", "value": "300To700"}
- [300 to 700]{"entity": "price", "value": "300To700"}
- from [300 to 700]{"entity": "price", "value": "300To700"}
- in range [300 and 700]{"entity": "price", "value": "300To700"}
- [More than 700]{"entity": "price", "value": "MT700"}
- [Above 700]{"entity": "price", "value": "MT700"}
- [above 700]{"entity": "price", "value": "MT700"}
- [> 700]{"entity": "price", "value": "MT700"}
- [>700]{"entity": "price", "value": "MT700"}
- I can do [more than 700]{"entity": "price", "value": "MT700"}
- [less than 300]{"entity": "price", "value": "LT300"} is my budget
- my budget is < [300]{"entity": "contact_email", "value": "LT300"}
- I am a rich kid. I can do [more than 700]{"entity": "price", "value": "MT700"}
- [300To700](price)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- heyo
- hola
- Hello there!
- Hey hi there!
- Hola
- hey buddy
- Hey
- heyyy
- hello there honey
- hello there

## intent:contact_id
- My email id is [maxmeier@gmail.com](contact_email)
- email id is [maxmeier@gmail.com](contact_email)
- email id is [abc@gmail.com](contact_email)
- email id is [abc@yahoo.com](contact_email)
- email id is [abc@rediff.com](contact_email)
- email id is [abc@upgrad.com](contact_email)
- email id is [abc@outlook.com](contact_email)
- email id is [abc@outlook.pq](contact_email)
- email id is [abc@xyz.pqr](contact_email)
- email id is [abc@gmail.co.in](contact_email)
- email id is [abc@yahoo.co.in](contact_email)
- email id is [abc@rediff.co.in](contact_email)
- email id is [abc@upgrad.co.in](contact_email)
- email id is [abc@outlook.co.in](contact_email)
- email id is [abc@outlook.pq.in](contact_email)
- email id is [abc@xyz.pqr.in](contact_email)
- yes, email id is [maxmeier@gmail.com](contact_email)
- send it to [maxmeier@gmail.com](contact_email)
- to [maxmeier@gmail.com](contact_email)
- Send it to [maxmeier@gmail.com](contact_email)
- [maxmeier@firma.de](contact_email)
- yes. Please send it to [xyz@gmail.com](contact_email)
- it is [manmanman@madhavi.com](contact_email)
- [madhavi.kodu@yahoo.com](contact_email)
- hello, the id is [jgerffr@gmail.com](contact_email)
- my id is [madhavi.koduganti@gmail.com](contact_email)
- my mail id is [r123@ttsi.cos](contact_email)
- [wwstei@grrr.wgo](contact_email)
- [iieta@ttya.com](contact_email)
- email id is [aagt@yytad.coww](contact_email)
- yes send it to [madhavi.koduganti@gmail.com](contact_email)
- send it to [happyhappybro@wasssuupp.co](contact_email)
- [blablablew@puppyinc.com](contact_email)
- [witty@humour.inc](contact_email)
- send it to [wwrtey@rediff.com](contact_email)
- my email ID is [wwalia@upgrad.com](contact_email)
- send it to [vikram@twitter.com](contact_email)
- send it to [whoswho@gmail.com](contact_email)
- yes. send it to [mkd@yahoo.co.in](contact_email)
- send it over to my butler's mail id. i think it is [mybutler@yahoo.co.in](contact_email)
- mail id is [madhavi.koduganti@gmail.com](contact_email)

## intent:restaurant_search
- [SIndian](cuisine)
- [NIndian](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [North American]{"entity": "cuisine", "value": "American"}
- [South Indian]{"entity": "cuisine", "value": "SIndian"}
- [South indian]{"entity": "cuisine", "value": "SIndian"}
- [south Indian]{"entity": "cuisine", "value": "SIndian"}
- [south indian]{"entity": "cuisine", "value": "SIndian"}
- [North Indian]{"entity": "cuisine", "value": "NIndian"}
- [North indian]{"entity": "cuisine", "value": "NIndian"}
- [north Indian]{"entity": "cuisine", "value": "NIndian"}
- [north indian]{"entity": "cuisine", "value": "NIndian"}
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [mumbai](location)
- [Lithuania](location)
- in [Gurgaon](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- [delhi](location)
- [central](location) [indian](cuisine) restaurant
- show me restaurants
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- search for restaurants
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants from [New Delhi]{"entity": "location", "value": "Delhi"}
- show me restaurants from [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- get me [italian](cuisine) restaurants in [bangalore](location)
- get me [italian](cuisine) restaurants from [bangalore](location)
- get me restaurants from [bangalore](location)
- please show me restaurants from Quilon[]{"entity": "location", "value": "Quilon"}
- I’m hungry. Looking out for some good restaurants
- Tiruchirapalli[]{"entity": "location", "value": "Tiruchirapalli"}
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- I am very hungry right now and about to become unconscious. I really need to eat somewhere. Can you please show me some restaurants?
- in [Bombay]{"entity": "location", "value": "Mumbai"}[Bombay]{"entity": "location", "value": "Mumbai"}
- Will you be able to let me know of some restaurants?
- In [Madurai](location)
- in [mumbai](location)
- bengaluru[]{"entity": "location", "value": "bengaluru"}
- I cannot tell you how hungry I am right now. I can totally devour a big elephant. I really need to find some [north indian]{"entity": "cuisine", "value": "NIndian"} restaurants in [Calicut]{"entity": "location", "value": "Kozhikode"}
- Can you suggest some good restaurants in [Rishikesh](location)
- Can you suggest some good restaurants in [Kolkata](location)
- Can you suggest some good restaurants in [kolkata](location)
- Can you show me some good [south indian]{"entity": "cuisine", "value": "SIndian"} restaurants in [Kurnool](location)
- can you show me restaurants in [below 300]{"entity": "price", "value": "LT300"}
- can you show me some [chinese](cuisine) restaurants
- in [Dehradun](location)
- can you show me some restaurants in [Vadodara](location)
- Can you show me some [south indian]{"entity": "cuisine", "value": "SIndian"} restaurants in price range [above 700]{"entity": "price", "value": "MT700"} in [Calicut]{"entity": "location", "value": "Kozhikode"}
- I want to know about some healthy [mexican]{"entity": "cuisine", "value": "Mexican"} restaurants in [Vadodara](location) for price range [between 300 and 700]{"entity": "price", "value": "300To700"}
- can you show me some great restaurants for price [less than 300]{"entity": "price", "value": "LT300"}
- in [Mysore](location)
- Can you show me some of my favourite non vegetarian [american]{"entity": "cuisine", "value": "American"} restaurants in [Maikala]{"entity": "location", "value": "Mangalore"} for the price range in [300 700]{"entity": "price", "value": "300To700"}?
- hello there. Show me some restaurants from [Chennai](location)
- Get me [mexican]{"entity": "cuisine", "value": "Mexican"} restaurants from [Chennai](location) in price range [above 700]{"entity": "price", "value": "MT700"}
- I wanna see hotels from [Bangalore](location)
- show me restaurants from [Ghaziabad](location)
- can you show me some hotels from [Indore](location)?
- can you show me some hotels from [Allahabad](location)
- I am hungry. I wanna know about nearby dineouts
- I wanna go to a [mexican]{"entity": "cuisine", "value": "Mexican"} restaurant in [Kohl]{"entity": "location", "value": "Aligarh"}
- Want to go to a dineout in [Holkar]{"entity": "location", "value": "Indore"}
- Can you please show me some hotels from [Chennai](location)
- can you please help me fine some [American](cuisine)  restaurants in [Hyderabad](location)?

## synonym:300To700
- 300-700
- between 300 and 700
- Rs. 300 to 700
- 300 to 700
- 300 and 700
- 300 700

## synonym:4
- four

## synonym:Ahmedabad
- Amdavad

## synonym:Ajmer
- Ajmeer
- Ajmir
- Azmer

## synonym:Aligarh
- Kohl
- Koil
- Aligad
- Aligadh
- Aligar

## synonym:Allahabad
- Prayagraj
- Prayag
- Illahabad

## synonym:American
- North American
- american
- america
- America

## synonym:Amravati
- Udumbravati
- Umbravati
- Amaravati

## synonym:Amritsar
- Ramdaspur

## synonym:Bareilly
- Nath Nagri
- Sanjashya

## synonym:Belgaum
- Belgaon

## synonym:Bhavnagar
- Kathiawar
- Kathiawad
- Bhaavnagar
- Bhaav nagar
- Bhav nagar

## synonym:Bhubaneswar
- Bhuvaneswar
- Toshali
- Kalinga
- Kalinga Nagar
- Nagar Kalinga
- Chakra Kshetra
- Ekamra Kanan
- Ekamra Kshetra
- Mandira Malini Nagari
- Mandira Malini Nagar

## synonym:Bijapur
- Vijayapura
- Vijaypura

## synonym:Chennai
- Madras

## synonym:Coimbatore
- Kovai
- Koyampuththoor
- Koyamputhoor

## synonym:Dehradun
- Dera Doon

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Erode
- Yellow City
- Turmeric City

## synonym:Firozabad
- Chandwar nager

## synonym:Ghaziabad
- Ghaziuddinnagar

## synonym:Goa
- Sindapur
- Sandabur
- Mahassapatam

## synonym:Gulbarga
- Kalaburagi

## synonym:Gurgaon
- Gurugram

## synonym:Guwahati
- Gauhati

## synonym:Hubli–Dharwad
- Dharwad
- Hubballi

## synonym:Indore
- Holkar

## synonym:Italian
- italy
- italian
- Italy

## synonym:Jabalpur
- Jubbulpore

## synonym:Jaipur
- Pink City

## synonym:Jalandhar
- Jullundur

## synonym:Jamnagar
- Nawanagar

## synonym:Jamshedpur
- Sakchi

## synonym:Jhansi
- Gateway of Bundelkhand
- Crossroads of India
- City of Rani Lakshmibai

## synonym:Jodhpur
- Blue City

## synonym:Kakinada
- Cocanada

## synonym:Kannur
- Cannanore
- Cananor
- Coonoor

## synonym:Kanpur
- Kanhapur

## synonym:Kochi
- Ernakulam
- Cochin

## synonym:Kolhapur
- Dakshin Kashi
- Colapore

## synonym:Kolkata
- Calcutta

## synonym:Kollam
- Quilon
- Coulao

## synonym:Kozhikode
- Calicut

## synonym:Kurnool
- Kandanavolu

## synonym:LT300
- Less than Rs. 300
- less than 300
- Less than 300
- 300
- <300
- < 300
- Lesser than Rs. 300
- below 300

## synonym:Lucknow
- Lakhanpur

## synonym:MT700
- More than 700
- Above 700
- above 700
- > 700
- >700
- more than 700

## synonym:Madurai
- Koodal
- Malligai Maanagar
- Naanmadakoodal
- Thirualavai

## synonym:Mangalore
- Maikala
- Kudla
- Mangalooru
- Mangalapuram
- Kodeyaala
- Kodial
- Manjarun

## synonym:Mathura
- Madhupura

## synonym:Meerut
- Meerat

## synonym:Mexican
- mexican
- mexico

## synonym:Moradabad
- Brass City
- Pital Nagri

## synonym:Mumbai
- Bombay
- Bambai

## synonym:Mysore
- Mysuru
- Maisuru

## synonym:NIndian
- North Indian
- North indian
- north Indian
- north indian
- North
- north

## synonym:Nagpur
- Nagpore

## synonym:Nashik
- Gulshanabad
- Nasik

## synonym:Patna
- Pataliputra
- Palibothra
- Kusumpur
- Pushpapura
- Azimabad

## synonym:Pondicherry
- Puducherry
- Pondy

## synonym:Pune
- poona

## synonym:Rajahmundry
- Rajamahendravaram
- Rajamandry
- Rajamundry
- Rajamandri

## synonym:Rajkot
- Chitranagri

## synonym:Ranchi
- Rachi

## synonym:Rourkela
- Steel City
- spat Mahanagar
- Engineering Hub

## synonym:SIndian
- South Indian
- South indian
- south Indian
- south indian
- South
- south

## synonym:Sangli
- Sahagalli

## synonym:Solapur
- Sandalpur
- Sonalpur

## synonym:Srinagar
- Pravasenpur

## synonym:Surat
- Suryanagari
- Surajpur
- Suryapur
- THE SILK CITY
- THE DIAMOND CITY
- THE GREEN CITY

## synonym:Thiruvananthapuram
- Trivandrum
- Trivendrum

## synonym:Thrissur
- Trichur
- Vrishabhadripuram

## synonym:Tiruchirappalli
- Trichinopoly
- Trichy
- Tiruchi
- Tiruchhi

## synonym:Tiruppur
- Tirupur

## synonym:Ujjain
- Ujjaini
- Avanti
- Avantika
- Avantikapuri

## synonym:Vadodara
- Baroda

## synonym:Varanasi
- Benares
- Banaras
- Kashi

## synonym:Vellore
- Velore
- Velluru

## synonym:Vijayawada
- Vijayavatika
- Bezawada
- Bejawada
- Vijayavada
- Bezavada

## synonym:Visakhapatnam
- Vizag
- Visakha
- Waltair

## synonym:Warangal
- Orugallu
- Ekasila Nagaram
- Ekasila
- Ekasila Nagari
- Omatikonda

## synonym:bangalore
- Bengaluru

## synonym:chinese
- Chinese
- chines
- Chines
- china
- China

## synonym:manasa.koduganti@gmail.com
- om

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg
- veggo
- vegan

## regex:contact_email
- ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:price
- [3,7]0{2}

## lookup:location
  ./CityList.txt
