#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import os
import time

headers = {
    'User-Agent': 'tfgm-notifier'
}

request_uri = "https://beta.tfgm.com/public-transport/stations/mediacityuk-tram"
audio_dir = "audio"

while True:

	print "Making HTTP request to " + request_uri
	response = requests.get(request_uri, headers=headers)
	html_doc = response.text
	soup = BeautifulSoup(html_doc, 'html.parser')

	depatures_tbody = soup.findAll('tbody', {"id" : "departure-items"})[0]
	tram_trs = depatures_tbody.findAll('tr',  {"class" : "tram"})

	trams = []
	for tram_tr in tram_trs:
		destination = tram_tr.findAll('td',  {"class" : "departure-destination"})[0].text
		wait_td = tram_tr.findAll('td',  {"class" : "departure-wait"})[0]
		wait_figure = wait_td.findAll('span',  {"class" : "figure"})[0].text
		wait_unit = wait_td.findAll('span',  {"class" : "unit"})[0].text
		trams.append({"destination": destination, "wait_figure": wait_figure, "wait_unit": wait_unit})
	print "Trams:"
	print trams
	print ""

	interesting_destinations = ["Piccadilly", "See Tram Front"]

	interesting_trams = []
	for tram in trams:
		if tram["destination"] in interesting_destinations:
			interesting_trams.append(tram)
	print "Interesting trams:"
	print interesting_trams
	print ""

	min_wait = 2
	max_wait = 12
	interesting_trams_within_acceptable_wait = []
	for tram in interesting_trams:
		wait = int(tram["wait_figure"])
		if wait <= max_wait and wait >= min_wait:
			interesting_trams_within_acceptable_wait.append(tram)

	print "Interesting trams within acceptable wait:"
	print interesting_trams_within_acceptable_wait
	print ""

	def play_audio(key):
		os.system("afplay " + audio_dir + "/"+key+".mp3")  

	for tram in interesting_trams_within_acceptable_wait:
		play_audio("the-next-tram-to")
		destination_key = tram["destination"].replace(" ", "-").lower()
		play_audio(destination_key)
		play_audio("departs-in")
		wait_key = tram["wait_figure"].replace(" ", "-").lower()
		play_audio(wait_key)
		play_audio("minutes")
		time.sleep(5)
	time.sleep(60)
