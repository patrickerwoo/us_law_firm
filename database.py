from pymongo import MongoClient


settings = {
    "ip": "localhost",
    "port": 27017,
    "db_name": "US_LawFirm",
    "set_name": "US_LawFirm_3"
}

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"],settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self,dic):
        print("insert")
        print(dic)
        self.my_set.insert_one(dic)

    def update(self,dic,newdic):
        print("update")
        print(dic)
        print(newdic)
        self.my_set.update(dic,newdic)

    def dbfind(self, dic):
        print("find")
        print(dic)
        data = self.my_set.find(dic)
        return data
