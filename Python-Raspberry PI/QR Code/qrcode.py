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
script name   : qr_code_with_secret_code_hiding.py
Functionality : Generates the QR Code with the secret invisible code written into it
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

import pyqrcode
url = pyqrcode.create('Type your secret text here')
url.svg('Ganesh.svg', scale=8)
print('qr code generated');								# Reads the secret code using QR code reader app
