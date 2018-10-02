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
script name   : serial_data_read.py
Functionality : Read the serial communication and displays in the console
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import serial
ser = serial.Serial('/dev/ttyACM0',9600)		# provide the data to read serial port details
												# Example linux: /dev/ttyACM0 or /dev/ttyACM1, windows: COM1, COM2
while 1:
	print(ser.readline())						# Prints the serial data in console
