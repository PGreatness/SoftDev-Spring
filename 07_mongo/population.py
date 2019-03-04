'''
Specialboard (Roster: Daniel Gelfand and Ahnaf Hasan)
SoftDev2 pd06
K07 -- Import/Export Bank
2019-03-04
'''


'''
Dataset used -- United States Population Table by Age (2010)
Hyperlink for dataset -- http://api.population.io/1.0/population/2010/United%20States/?format=json

Import Mechanism:
The import mechanism that we used was to run a subprocess, or a child process, that runs the mongoimport command
along with the neccessary parameters. The subprocess runs before the defined functions in order to make sure the
data is in the database.
'''
import subprocess  # used to run a child process that imports the json data

import pymongo

SERVER_ADDR="206.189.75.99"
FILE="population.json"
connection=pymongo.MongoClient(SERVER_ADDR)
command=f"mongoimport --host {SERVER_ADDR} --drop --db specialboard --collection population --file {FILE} --jsonArray" # "--jsonArray" needs to be included since JSON file is inclosed in an array
child=subprocess.run(command) 
db = connection.specialboard
collection = db.population


def get_population_age(age):
    '''returns population data for a given age'''
    return collection.find( {"age": age })[0]

def get_population_year(year):
    '''returns population data for a given year'''
    return collection.find( {"year": year })[0]

print( get_population_age(60) )

def get_year(totalPop):
    '''returns year(s) when total population equals the one provided'''
    lout = []

    for doc in collection.find( {"total": totalPop} ):
        lout.append(doc)
    return lout

print( get_year(4430000) )

#defaults to female population
def get_years_gte(numSex, female = True):
    '''returns years when female or male population was greater than or equal to num provided'''
    lout = []
    if(female):
        for doc in collection.find({"females": {"$gte": numSex}}):
            lout.append(doc)
    # look at males
    else:
        for doc in collection.find({"males": {"$gte": numSex}}):
            lout.append(doc)
    return lout

print( get_years_gte( 2300000 ) )
print( get_years_gte( 1300000, False ) )

def get_years_lte(numSex, female = True):
    '''returns years when female or male population was less than or equal to num provided'''
    lout = []

    if(female):
        for doc in collection.find({"females": {"$lte": numSex}}):
            lout.append(doc)
    # look at males
    else:
        for doc in collection.find({"males": {"$lte": numSex}}):
            lout.append(doc)
    return lout

print( get_years_lte( 100000 ) )
print( get_years_lte( 100000, False ) )

def look_for_more(female = True):
    '''Returns years in which population of given sex is larger than the other. True for female (default), false for male'''
    out = []
    for doc in collection.find():
        if (female):
            if (doc["males"] > doc["females"]):
                out.append(doc)
        else:
            if (doc["males"] < doc["females"]):
                out.append(doc)
    return out

print(look_for_more(True))