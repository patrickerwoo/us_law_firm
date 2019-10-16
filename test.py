from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
from database import MyMongoDB

mongo = MyMongoDB()
count = 0
for firm in mongo.dbfind({}):

    main_state = firm['main_state']
    if isinstance(main_state,str) == False:
        count += 1
        print(count)
        print(main_state)

