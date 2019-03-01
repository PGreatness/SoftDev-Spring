'''
GoodQuestion -- Roster: Ahnaf Hasan and Britni Canale
SoftDev2 pd06
K06 -- Yummy Mongo Py
2019-02-28
'''
import pymongo as m

SERVER_ADDR = "206.189.75.99"
client = m.MongoClient(SERVER_ADDR, 27017)
db = client.test

restaurants = db.restaurants

def borough(borough):
    bronxRestaurants = restaurants.find(
        {
            "borough": borough
        }
    )
    for doc in bronxRestaurants:
        print(doc)

def zipcode(code):
    zipRestaurants = restaurants.find(
        {
            "zipcode": code
        }
    )
    for doc in zipRestaurants:
        print(doc)

def gradezip(zipCode, grade):
    zipARestaurants = restaurants.find(
        {
            "zipcode":zipCode,
            "grade":grade
        }
    )
    for doc in zipARestaurants:
        print(doc)

def gradelesszip(grade, zipCode):
    zipLssRestaurants = restaurants.find(
        {
            "zipcode": zipCode,
            "grade": {"$lt":grade}
        }
    )
    for doc in zipLssRestaurants:
        print(doc)

# borough("Manhattan")
# zipcode("11234")
# gradezip("11012", "B")
gradelesszip("A", "12311")