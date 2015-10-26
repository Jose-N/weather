#! python3
# weather.py
# Scrapes http://www.accuweather.com/ to grab weather information that can be called from command line

import sys,requests
from bs4 import BeautifulSoup

# Activate from command line
if len(sys.argv) > 1:
	# Use if statments to determine what to do
	# Get current weather
	if "current" == ''.join(sys.argv[1]):
		todayRes = requests.get("http://www.accuweather.com/en/us/philadelphia-pa/19107/weather-forecast/350540")
		todayRes.raise_for_status()
		todaySoup = BeautifulSoup(todayRes.text, "html.parser")
		todayWeather = todaySoup.select("#feed-main .temp")
		currentWeather = todayWeather[0].getText()
		print("It's " + currentWeather + "F right now.")
	# Get todays weather
	# Get hourly weather
	#if "hourly" == ''.join(sys.argv[1]):
	# 10 day weather forecast
	#if "10day" == ''.join(sys.argv[1]):

# TODO: Add ablilty to text myself in the morning to bring umbrella if it is going to rain