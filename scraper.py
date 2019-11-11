import requests
from bs4 import BeautifulSoup
import re
import datetime
import json
import pandas

def get_menu():
    r = requests.get('https://www.seezeit.com/essen/speiseplaene/mensa-giessberg/')
    soup = BeautifulSoup(r.text, features="lxml")
    food = soup.select("div.contents_aktiv div.speiseplanTagKat")
    today = str(datetime.date.today())
    tbl = []
    for i in food:
        vegetarian, vegan = [0, 0]
        regex = re.compile(r"\(.+?\)")
        cat = i.select(".category")
        tit = i.select(".title")
        veg = i.select(".title_preise_2")
        for c, t, v in zip(cat, tit, veg):
            if(v.select(".Veg")):
                vegetarian = 1
            elif(v.select(".Vegan")):
                vegetarian, vegan = [1]*2
            ret_tuple = (today,
                        re.sub(regex, '', c.get_text()),
                        re.sub(regex, '', t.get_text()).replace(" | ", ", "),
                        vegetarian, vegan)
            tbl.append(ret_tuple)
    return((tbl))
