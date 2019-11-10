import mysql.connector
import urllib.request
from bs4 import BeautifulSoup
html = urllib.request.urlopen('https://www.wienerlinien.at/eportal3/ep/channelView.do/pageTypeId/66526/channelId/-50038')

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())
