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
		currentRes = requests.get("http://www.accuweather.com/en/us/philadelphia-pa/19107/weather-forecast/350540")
		currentRes.raise_for_status()
		currentSoup = BeautifulSoup(currentRes.text, "html.parser")
		currentCond  = currentSoup.select(".cond")[0].getText()
		currentWeather = currentSoup.select("#feed-main .temp")
		currentTemp = currentWeather[0].getText()
		print("It's " + currentTemp + "F right now, and it is " + currentCond)
	# Get todays weather
	if "today" == ''.join(sys.argv[1]):
		todayRes = requests.get("http://www.accuweather.com/en/us/philadelphia-pa/19107/daily-weather-forecast/350540?day=1")
		todayRes.raise_for_status()
		todaySoup = BeautifulSoup(todayRes.text, "html.parser")
		todayHiTemp = todaySoup.select(".day .temp")[0].getText()
		todayLowTemp = todaySoup.select(".night .temp")[0].getText()
		todayWeather = todaySoup.select(".day .content p")[4].getText()
		tonightWeather = todaySoup.select(".night .content p")[4].getText()
		print("The high today is " + todayHiTemp + "F" + " the low today is " + todayLowTemp + "F")
		print( "Today is going to be " + todayWeather + " with " + tonightWeather + " at night")
	# Get hourly weather
	#if "hourly" == ''.join(sys.argv[1]):
	# 10 day weather forecast
	#if "10day" == ''.join(sys.argv[1]):

# TODO: Add ablilty to text myself in the morning to bring umbrella if it is going to rain