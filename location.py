from database import MyMongoDB
import re
from request import get_browser
import time
import request
from bs4 import BeautifulSoup

regex = r"\((\d).+ocation"

def multi_location():
    mongo = MyMongoDB()
    for firm in mongo.dbfind({}):
        location = firm['location']
        id = firm['_id']
        if "ocation" in location:
            mongo.update({'_id': id},{'$set':{'multi_location': 1}})
            matches = re.finditer(regex, location, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                num_location = int(match.group(1))
                mongo.update({'_id': id}, {'$set': {'num_location': num_location}})
        elif "ocation" not in location:
            mongo.update({'_id': id},{'$set':{'multi_location': 0}})
            mongo.update({'_id': id}, {'$set': {'num_location': 0}})



def get_location(browser, firm_url): #not state
    browser.get(firm_url)
    browser.maximize_window()
    time.sleep(1)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    aas = soup.find_all('div', {'class': 'office-address small-10 columns'})
    locations = []
    for a in aas:
        aa = a.a.get_text()
        locations.append(aa)
    return locations

def get_firm_url(firm_link):
    link_ls = firm_link.split('/')
    del link_ls[-2]
    firm_url = "/".join(link_ls)
    return firm_url

def mongo_get_firm_link():
    global firm
    mongo = MyMongoDB()
    browser = get_browser()
    for firm in mongo.dbfind({'multi_location': {'$eq' : 1}}):
        id = firm['_id']
        firm_link = firm['firm_link']
        firm_url = get_firm_url(firm_link)
        locations = get_location(browser, firm_url)
        mongo.update({'_id' : id}, {'$set' : {'locations': locations}})


if __name__ == "__main__":
    multi_location()
    mongo_get_firm_link()

