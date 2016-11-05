#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'tfgm-notifier'
}

request_uri = "https://beta.tfgm.com/public-transport/stations/mediacityuk-tram"

print "Making HTTP request to " + request_uri
response = requests.get(request_uri, headers=headers)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

depatures_tbody = soup.findAll('tbody', {"id" : "departure-items"})[0]
tram_trs = depatures_tbody.findAll('tr',  {"class" : "tram"})

for tram_tr in tram_trs:
	destination = tram_tr.findAll('td',  {"class" : "departure-destination"})[0].text
	wait_td = tram_tr.findAll('td',  {"class" : "departure-wait"})[0]
	wait_figure = wait_td.findAll('span',  {"class" : "figure"})[0].text
	wait_unit = wait_td.findAll('span',  {"class" : "unit"})[0].text
	print "Tram to " + destination + " leaves in " + wait_figure + " " + wait_unit