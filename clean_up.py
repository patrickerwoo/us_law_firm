from database import MyMongoDB, MyMongoDB_2
import pymongo


def get_old_data():
    mongo = MyMongoDB()
    mongo_2 = MyMongoDB_2()
    for firm in mongo.dbfind({}):
        id = firm['title']
        link = firm['firm_link']
        main_state = firm['main_state']
        try:
            states = firm['states']
            try:
                mongo_2.insert({'_id': id, 'link': link, 'main_state':main_state, 'states':states})
            except pymongo.errors.DuplicateKeyError:
                continue
        except KeyError:
            try:
                mongo_2.insert({'_id': id, 'link': link, 'main_state': main_state})
            except pymongo.errors.DuplicateKeyError:
                continue


if __name__ == "__main__":
    get_old_data()
