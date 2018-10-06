#!/usr/bin/python2.7

"""
------------------------------------------
		License Information
------------------------------------------
        GNU GENERAL PUBLIC LICENSE
        Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. 
https://fsf.org/ Everyone is permitted to copy and 
distribute verbatim copies of this license document, 
but changing it is not allowed.

Note: For detailed license information, 
please read the LICENSE file in the repository[Repository Name: Projects-IoT-Python-Embedded-C]
"""

"""
script name   : weather_data.py
Functionality : Checks the weather data from weatherapi.org source and display into console
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import requests
import weatherconfig
from pprint import pprint		# pprint will display the data in structured format

api_key = 'Type your weather api key here which you got from weatherapi.org services'

place = "London"				# Type the location name which you want to check the weather 

url = "http://api.openweathermap.org/data/2.5/weather?q=" + place + "&appid=" + api_key + "&units=metric"
response = requests.get(url)
data = response.json()
pprint(data)

