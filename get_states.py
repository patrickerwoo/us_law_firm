from database import MyMongoDB
import re
from request import get_browser
import time
import request
from bs4 import BeautifulSoup



def get_states(locations):
    state = set()
    for loc in locations:
        loc_ls = loc.split(",")
        locs = loc_ls[-1]
        locs = locs.strip()
        state.add(locs)
    return state

def mongo_states():
    mongo = MyMongoDB()
    for firm in mongo.dbfind({'locations': {'$exists' : "true"}}):
        id = firm['_id']
        locations = firm['locations']
        states = get_states(locations)
        states = list(states)
        mongo.update({'_id' : id}, {'$set' : {'states': states}})


if __name__ == "__main__":
    mongo_states()


