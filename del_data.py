from database import MyMongoDB_2, MyMongoDB_3



def del_data():
    global firm
    mongo_2 = MyMongoDB_2()
    mongo_3 = MyMongoDB_3()
    for firm in mongo_2.dbfind({'states':{'$exists': 'true'}}):
        id = firm['_id']
        states = firm['states']
        link = firm['link']
        main_state = firm['main_state']
        if len(states) > 1:
            mongo_3.insert({'_id': id, 'states': states, 'link': link, 'main_state': main_state})

if __name__ == "__main__":
    del_data()

