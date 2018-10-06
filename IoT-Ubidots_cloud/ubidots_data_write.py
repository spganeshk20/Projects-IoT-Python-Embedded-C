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
script name   : ubidots_data_write.py
Functionality : Connects to Ubidots cloud and writes the data into it from any edge devices
Created on    : 21 SEP 2016
"""

__author__ = 'Ganesh'

import time
from ubidots import ApiClient

for i in range(0,5):									# Attempting to connect to ubidots cloud
    try:
        print ("Requesting Ubidots token");
        api = ApiClient('Add your client id here from ubidots cloud') 			# Connect to Ubidots
        break
    except:
        print ("No internet connection, retrying...");
        time.sleep(5)

a0 = 4;																			# Sample input values to write into cloud
a1 = 5;																			# Sample input values to write into cloud

while(1):
    api.save_collection([{'variable': '57a981467625425e2ffe0550','value':a0}, 
    	{'variable': '57a981507625425dae56f691','value':a1}])				# Writes the data into cloud using ubidots write API
