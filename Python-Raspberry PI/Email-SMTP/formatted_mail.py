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
script name   : formatted_mail.py
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
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "xxxxxxxxxxxxxxxxxxxx"
toaddr = "xxxxxxxxxxxxxxx"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "test mail"
 
body = "Hai Dude, This is test mail for alert notification"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "from email id password")			# from email id and password to login to your mail account
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
