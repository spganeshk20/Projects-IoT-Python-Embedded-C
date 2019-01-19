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
please read the LICENSE file in the repository
[Repository Name: Projects-IoT-Python-Embedded-C]
"""

"""
script name   : config.py
Functionality : config information of the intruder alert system
Created on    : 19 JAN 2019
"""

__author__ = 'Ganesh'

# Board Pin Assignments
LED_PIN = 7
PIR_SENSOR_DIGITAL_OUTPUT_PIN = 11
ULTRASONIC_SENSOR_TRIGGER_PIN = 23
ULTRASONIC_SENSOR_ECHO_PIN = 24

# Library Constants
NUMERIC_CONSTANT_ZERO = 0
NUMERIC_CONSTANT_ONE = 1
NUMERIC_CONSTANT_TWO = 2
NUMERIC_CONSTANT_FIVE = 5
NUMERIC_CONSTANT_TEN = 10
NUMERIC_CONSTANT_FIFTEEN = 15
NUMERIC_CONSTANT_TWENTY = 20
NUMERIC_CONSTANT_THIRTY = 30
NUMERIC_CONSTANT_SIXTY = 60
NUMERIC_CONSTANT_EIGHTY = 80
STR_SYMBOL = '-'
STR_SYMBOL_STAR = '*'
STR_SAFE = 'SAFE'
STR_BREACH = 'BREACH'
STR_LAST = 'Last'
STR_RECENT = 'Recent'
STR_ON = 'ON'
STR_OFF = 'OFF'
STR_DATA = 'DATA'
STR_SYSTEM = 'SYSTEM'
STR_NONE = 'NONE'

# Cloud Constants
DATA_CHANNEL_ID = 'xxxxxxxx'
DATA_CHANNEL_WRITE_API_KEY = 'xxxxxxxxxxxxx'
DATA_CHANNEL_READ_API_KEY = 'xxxxxxxxxxxxxx'
SYSTEM_CHANNEL_ID = 'xxxxxxxx'
SYSTEM_CHANNEL_WRITE_API_KEY = 'xxxxxxxxxxxxxx'
SYSTEM_CHANNEL_READ_API_KEY = 'xxxxxxxxxxxxxxxx'

