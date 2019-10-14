import re
from database import MyMongoDB
from database import MyMongoDB_2


def get_main_state(location):
    regex = r" ([A-Z][A-Z])"
    matches = re.finditer(regex, location, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        state = match.group(1)
        return state

def mongo_main_states():
    mongo = MyMongoDB()

    for firm in mongo.dbfind({'location': {'$exists' : "true"}}):
        id = firm['_id']
        location = firm['location']
        state = get_main_state(location)
        mongo.update({'_id' : id}, {'$set' : {'main_state': state}})



if __name__ == "__main__":
    mongo_main_states()
