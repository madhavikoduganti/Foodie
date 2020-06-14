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
- thanks

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
- hi
- hi
- hello
- heyo
- hola
 
 
## intent:contact_id
- My email id is [maxmeier@firma.de](contact_email)
- email id is [maxmeier@firma.de](contact_email)
- send it to [maxmeier@firma.de](contact_email)
- to [maxmeier@firma.de](contact_email)
- Send it to [maxmeier@firma.de](contact_email)
- [maxmeier@firma.de](contact_email)
- [bot-fan@bots.com](contact_email)
- [maxmeier@firma.de](contact_email)
- [bot-fan@bots.com](contact_email)

## regex:contact_email
- ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$

## intent:restaurant_search


- [SIndian](cuisine)
- [NIndian](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [North American](cuisine:American)
- [South Indian](cuisine:SIndian)
- [South indian](cuisine:SIndian)
- [south Indian](cuisine:SIndian)
- [south indian](cuisine:SIndian)
- [North Indian](cuisine:NIndian)
- [North indian](cuisine:NIndian)
- [north Indian](cuisine:NIndian)
- [north indian](cuisine:NIndian)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [mumbai](location)
- [Lithuania](location)
- in [Gurgaon](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- [mumbai](location)
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
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me [chines](cuisine:chinese) restaurants from [New Delhi](location:Delhi)
- show me restaurants from [New Delhi](location:Delhi)
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





## lookup:location
./CityList.txt

## synonym:4
- four

## synonym:Delhi
- New Delhi
- Dilli

## synonym:bangalore
- Bengaluru

## synonym:Ahmedabad
- Amdavad

## synonym:Chennai
- Madras

## synonym:Kolkata
- Calcutta

## synonym:Mumbai
- Bombay
- Bambai

## synonym:Pune
- poona

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

## synonym:Coimbatore
- Kovai
- Koyampuththoor
- Koyamputhoor

## synonym:Dehradun
- Dera Doon

## synonym:Erode
- Yellow City
- Turmeric City

## synonym:Firozabad
- Chandwar nager

## synonym:Ghaziabad
- Ghaziuddinnagar

## synonym:Gulbarga
- Kalaburagi

## synonym:Gurgaon
- Gurugram

## synonym:Guwahati
- Gauhati

## synonym:Indore
- Holkar

## synonym:Hubli–Dharwad
- Dharwad
- Hubballi

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

## synonym:Kochi
- Ernakulam
- Cochin

## synonym:Kanpur
- Kanhapur

## synonym:Kolhapur
- Dakshin Kashi
- Colapore

## synonym:Kollam
- Quilon
- Coulao

## synonym:Kollam
- Quilon
- Coulao

## synonym:Kozhikode
- Calicut

## synonym:Kurnool
- Kandanavolu

## synonym:Lucknow
- Lakhanpur

## synonym:Madurai
- Koodal
- Malligai Maanagar
- Naanmadakoodal
- Thirualavai

## synonym:Mathura
- Madhupura

## synonym:Goa
- Sindapur
- Sandabur
- Mahassapatam

## synonym:Mangalore
- Kudla
- Mangalooru
- Mangalapuram
- Kodeyaala
- Kodial
- Maikala
- Manjarun

## synonym:Meerut
- Meerat

## synonym:Mysore
- Mysuru
- Maisuru

## synonym:Moradabad
- Brass City
- Pital Nagri

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

## synonym:Allahabad
- Prayag
- Prayagraj
- Illahabad

## synonym:Rajkot
- Chitranagri

## synonym:Rajahmundry
- Rajamahendravaram
- Rajamandry
- Rajamundry
- Rajamandri


## synonym:Ranchi
- Rachi

## synonym:Rourkela
- Steel City
- spat Mahanagar
- Engineering Hub

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

## synonym:Bijapur
- Vijayapura
- Vijaypura

## synonym:Vadodara
- Baroda

## synonym:Varanasi
- Benares
- Banaras
- Kashi

 

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

## synonym:Vellore
- Velore
- Velluru

## synonym:Warangal
- Orugallu
- Ekasila Nagaram
- Ekasila
- Ekasila Nagari
- Omatikonda


## synonym:Mexican
- mexican
- mexico

## synonym:Italian
- italy
- italian
- Italy

## synonym:American
- america
- american
- America


## synonym:SIndian
- South Indian
- South
- south
- south indian
- south Indian
- South indian


## synonym:NIndian
- North Indian
- North
- north
- north indian
- north Indian
- North indian


## synonym:chinese
- chines
- Chinese
- Chines
- china
- China

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg
- veggo
- vegan









## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:price
- [3,7]0{2}


