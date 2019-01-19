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

__author__ = 'Ganesh'

"""
script name   : utils.py
Functionality : Module includes the reusable function
Created on    : 19 JAN 2019
"""

# Global Import
import logging
import datetime


def print_msg(msg):
    """
    Function name	 : print_msg
    Functionality	 : prints the message on the console
    Function Invoked : None
    Return value	 : None
    """
    try:
        print(str(msg))
    except Exception as e_obj:
        print 'EXCEPTION: In print_msg(), due to - %s' % e_obj
