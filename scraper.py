import mysql.connector
import urllib.request
from bs4 import BeautifulSoup
import re
html = urllib.request.urlopen('https://www.wienerlinien.at/eportal3/ep/channelView.do/pageTypeId/66526/channelId/-50038')

soup = BeautifulSoup(html, "html.parser")

info = soup.find_all('h2', {"class":"heading-type03"})
print(info)

#<h2 class="heading-type03">87A : Verkehrsunfall</h2>

#<div class="editor-output ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion-content-active" id="ui-accordion-2-panel-0" aria-labelledby="ui-accordion-2-header-0" role="tabpanel" aria-expanded="true" aria-hidden="false" style="display: block;">Nach einer Fahrtbehinderung kommt es auf der Linie 60 zu unterschiedlichen Intervallen.</div>
