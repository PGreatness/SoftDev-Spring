'''
WIP, error in connection. may not work
'''

import pymongo as m

SERVER_ADDR = "206.189.75.99"
client = m.MongoClient(SERVER_ADDR, 27017)
db = client.test

restaurants = db.restaurants

bronxRestaurants = restaurants.find(
    {
        "borough":"Bronx"
    }
)

zipRestaurants = restaurants.find(
    {
        "zipcode":"11223"
    }
)

zipARestaurants = restaurants.find(
    {
        "zipcode":"11223",
        "grade":"A"
    }
)

zipLssRestaurants = restaurants.find(
    {
        "zipcode":"11223",
        "grade": {$lt:400}
    }
)