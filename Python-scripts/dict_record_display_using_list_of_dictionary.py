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
script name   : dict_record_display_using_list_of_dictionary.py
Functionality : List of dictionary and display the data based on the run-time user input
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'


record=["gk", "gokul"]
gk=dict()
gk['Name']="Ganesh"
gk['Age']=22
gk['Designation']="ASE"

gokul=dict()
gokul['Name']="Gokul"
gokul['Age']=22
gokul['Designation']="ASE"

print "Available people records: ",record
name_input=input("Enter the name to search and view the records: ")
print name_input
