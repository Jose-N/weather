#! python3
# weather.py
# Scrapes http://www.wunderground.com/ to grab weather information that can be called from command line

import sys,request
for bs4 import BeautifulSoup

# Activate from command line
if len(sys.argv) > 1:
	# Use if statments to determine what to do
	# Get current weather
	if "today" == ''.join(sys.argv[1]):
	# Get hourly weather
	if "hourly" == ''.join(sys.argv[1]):
	# 10 day weather forecast
	if "10day" == ''.join(sys.argv[1]):

# TODO: Add ablilty to text myself in the morning to bring umbrella if it is going to rain