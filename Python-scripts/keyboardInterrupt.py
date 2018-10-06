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
script name   : keyboardInterrupt.py
Functionality : Interrupt the continuous execution by ctrl+c keyboard button press
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import signal
import time

def close():
	exit()

while True:
	try:	
		print("To Interrupt the print, press ctrl+c")
		time.sleep(0.5)		
	except KeyboardInterrupt:
		print("Interrupted, terminal going to close after 3 seconds of sleep")
		time.sleep(3)
		close()

