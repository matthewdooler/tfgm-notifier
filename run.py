#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'tfgm-notifier'
}

request_uri = "https://beta.tfgm.com/public-transport/stations/mediacityuk-tram"

response = requests.get(request_uri, headers=headers)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

print html_doc

#conversation_divs = soup.findAll('div', {"class" : "conversation"})