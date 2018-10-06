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
script name   : espeak.py
Functionality : Spells the given string via system audio speaker
Created on    : 21 AUG 2016
"""

from espeak import espeak

espeak.synth('You are listening to GK Studio channel') # Write the string to be spelled out via system audio speaker
