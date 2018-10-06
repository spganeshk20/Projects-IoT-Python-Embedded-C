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
script name   : led_on_off.py
Functionality : Turn ON/OFF the Raspberry pi Led
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.cleanup()
gpio.setwarnings(False)
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
print "Lights On"
gpio.output(7,gpio.HIGH)
gpio.output(11,gpio.HIGH)
time.sleep(2)
gpio.output(7,gpio.LOW)
gpio.output(11,gpio.LOW)




