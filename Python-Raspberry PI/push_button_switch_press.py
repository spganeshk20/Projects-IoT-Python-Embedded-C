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
script name   : push_button_switch_press.py
Functionality : Detects whether the push button switch is pressed or not
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'


import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.cleanup()
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(11,gpio.IN)

while True:
        inputValue = gpio.input(11)
        if(inputValue == 0):
                print("Pressed")
        time.sleep(0.2)


