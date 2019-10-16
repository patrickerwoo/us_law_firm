from selenium import webdriver
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pymongo
import requests
import scrapy
from selenium.webdriver.common.keys import Keys
from database import MyMongoDB
from selenium.webdriver.support.ui import Select
import states
import selenium

def get_browser():
    browser = webdriver.Chrome(executable_path=r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    return browser



def find_law_firm(html):
    soup = BeautifulSoup(html,"lxml")
    div = soup.find_all('div', {'class' : 'large-9 medium-12 columns card__content--details'})
    mongo = MyMongoDB()
    for d in div:
        law_firm = {}
        title = d.find_all('li', {'class': 'detail_title'})
        location = d.find_all('li', {'class' : 'detail_location'})
        link = d.find_all('a', href=True)
        link = link[1]
        for tit in title:
            t = tit.a.get_text()
            law_firm['title'] = t.strip()
        law_firm['firm_link'] = link['href']
        for loc in location:
            l = loc.get_text()
            law_firm['location'] = l.strip()
        law_firm['_id'] = law_firm['title'] + law_firm['location']
        try:
            mongo.insert(law_firm)
        except pymongo.errors.DuplicateKeyError as e:
            continue

def change_page(browser):
    for i in range(0,4):
        time.sleep(0.5)
        try:
            n = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[4]/div[2]/div/div/ul/li[4]/a")
            browser.execute_script("arguments[0].click();", n)
        except:
            continue

        time.sleep(2)

        html2 = browser.page_source
        find_law_firm(html2)

def change_sort(browser):
    for i in range(2,6):
        try:
            sort = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[3]/div/div/div[2]/nav/div[1]/a")
            time.sleep(0.5)
            browser.execute_script("arguments[0].click();", sort)

            time.sleep(1)

            sort2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[3]/div/div/div[2]/nav/div[1]/ul/li[%s]/a" % (i))
            browser.execute_script("arguments[0].click();", sort2)

            time.sleep(2)

            try:
                select = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[4]/div[2]/div/div/div[3]/a")
                browser.execute_script("arguments[0].click();", select)
            except selenium.common.exceptions.StaleElementReferenceException as e:
                continue

            time.sleep(1)

            s = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[4]/div[2]/div/div/div[3]/ul/li[3]/a")
            browser.execute_script("arguments[0].click();", s)

            time.sleep(2)

            html = browser.page_source
            find_law_firm(html)

            change_page(browser)
        except:
            continue

def change_star(browser):
    for i in range(1,7):
        star =  browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[4]/div[1]/div[1]/aside/ul/li[3]/div/ul/li[%s]/input" % (i))
        browser.execute_script("arguments[0].click();", star)
        time.sleep(2)
        change_sort(browser)


def main():
    browser = get_browser()
    for state in states.states:
        browser.get("https://www.martindale.com/litigation-lawyers/" + state)
        browser.maximize_window()

        time.sleep(1)

        choose1_elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[3]/div/div/div[1]/nav/ul/li[2]/span[1]")
        choose1_elem.click()
        time.sleep(2)

        select = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[4]/div[2]/div/div/div[3]/a")
        browser.execute_script("arguments[0].click();",select)

        time.sleep(1)

        s = browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/div[14]/div[4]/div[2]/div/div/div[3]/ul/li[3]/a")
        browser.execute_script("arguments[0].click();",s)

        time.sleep(2)

        html = browser.page_source
        find_law_firm(html)

        change_page(browser)

        time.sleep(2)

        change_sort(browser)

        change_star(browser)




if __name__ == "__main__":
    main()





