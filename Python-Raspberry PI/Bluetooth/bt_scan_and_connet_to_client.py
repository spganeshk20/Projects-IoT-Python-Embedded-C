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
Functionality : Bluetooth scans the nearby devices and stores in the dictionary,
				Accepts the Bluetooth device name to be connected from the user and establish the connection
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import bluetooth

nearby_devices =[]
nearby_devices = bluetooth.discover_devices(lookup_names = True)

bluetooth= {}

for addr, name in nearby_devices:
	bt_addr=addr
	bt_name=name
	bluetooth[bt_name]=bt_addr

print 'Available bluetooth devices are: '	

for bt_name in bluetooth.keys(): 
	print bt_name
user_input=input()

def client(bt_address):
	bd_addr = str(bt_address);  #BT address of a raspberry pi to which data have to transfer
	port = 1
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port))
	while 1:	
		message=raw_input("Enter the message to send: ");
		if message == "stop":
			sock.send(message)
			sock.close()
			exit()
		else:
			sock.send(message)
			print("To quit bluetooth communication type 'stop' without quotes")
