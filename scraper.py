#import mysql.connector
import requests
from bs4 import BeautifulSoup
import re

def get_menu():
    r = requests.get('https://www.seezeit.com/essen/speiseplaene/mensa-giessberg/')
    soup = BeautifulSoup(r.text, features="lxml")
    food = soup.select("div.contents_aktiv div.speiseplanTagKat")
    for i in food:
        cat = i.select(".category")
        tit = i.select(".title")
        pri = i.select(".preise")
