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
script name   : send_mail.py
Functionality : Sends the email from any gmail account to 'any To email id' user
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'

"""
Note: Allow less secure apps to access your Gmail account
Sign into Gmail.
Go to the “Less secure apps” section in My Account.
Next to “Allow less secure apps: OFF,” select the toggle switch to turn on. 
(Note to G Suite users: This setting is hidden if your administrator has locked less secure app account access.)
"""

import smtplib

content = "Type your content here to send to user"		
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('your_email@gmail.com','your_email_password')
mail.sendmail('from_email_id','to_email_id', content) 
mail.close()
print("Sent")
