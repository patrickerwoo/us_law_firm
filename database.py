from pymongo import MongoClient


settings = {
    "ip": "localhost",
    "port": 27017,
    "db_name": "US_LawFirm",
    "set_name": "US_LawFirm_3"
}

settings_2 = {
    "ip": "localhost",
    "port": 27017,
    "db_name": "US_LawFirm",
    "set_name": "US_LawFirm_3_2"
}

settings_3 = {
    "ip": "localhost",
    "port": 27017,
    "db_name": "US_LawFirm",
    "set_name": "US_LawFirm_3_3"
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
class MyMongoDB_2(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings_2["ip"],settings_2["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings_2["db_name"]]
        self.my_set = self.db[settings_2["set_name"]]

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

    def dbdel(self, dic):
        self.my_set.delete_one(dic)

class MyMongoDB_3(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings_3["ip"],settings_3["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings_3["db_name"]]
        self.my_set = self.db[settings_3["set_name"]]

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

    def dbdel(self, dic):
        self.my_set.delete_one(dic)