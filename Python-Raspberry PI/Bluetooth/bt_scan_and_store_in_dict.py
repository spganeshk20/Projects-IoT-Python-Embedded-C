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
script name   : bt_scan_and_store_in_dict.py
Functionality : Bluetooth scans the nearby devices and stores in the dictionary
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import bluetooth

print 'Master BT is scanning to display the available nearby devices:'

nearby_devices = []
nearby_devices = bluetooth.discover_devices(lookup_names = True)

bluetooth = {}
bluetooth_counter = {}
counter=0
for addr, name in nearby_devices:
	bt_addr=addr
	bt_name=name
	bluetooth[bt_name]=bt_addr
	counter=counter+1;
	bluetooth_counter[counter]=bt_name

for bt_number,bt_name in bluetooth_counter.items():
	print bt_number,'-',bt_name

user_input = input("Enter the device number to get connect: ");
print user_input



