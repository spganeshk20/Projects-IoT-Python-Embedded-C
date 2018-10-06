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
script name   : out_patient_data_entry_using_list_of_dictionary.py
Functionality : Collects the out patient details from the user at run-time and stores in the list of dictionaries
Created on    : 21 AUG 2016
"""

__author__ = 'Ganesh'


print("Welcome to GK Hospital care")						# Outpatient monitoring system
patientName = list()
patientAge = list()
patientAddress = list()


def recordUpdate():
	record=["gk", "gokul"]
	gk=dict();
	gk['Name']="Ganesh";
	gk['Age']=22;
	gk['Designation']="ASE"

	gokul=dict();
	gokul['Name']="Gokul";
	gokul['Age']=22;
	gokul['Designation']="ASE"


def recordDisplay():
	print "Available people records: ", record
	name_input=input("Enter the name to search his records: ")
	print name_input


def dataUpdateDisplay():
	print 'Updated data display'
	print patientName, patientAge, patientAddr


def dataUpdate(name,age,addr):
	patientName.append(name)
	patientAge.append(age)
	patientAddr.append(addr)
	print 'Data updated'
	dataUpdateDisplay()


def patientDetails():
	userName=input('Enter your name: ')
	userAge=input('Enter your age: ')
	UserAddr=input('Enter your address: ')
	dataUpdate(username,userAge,userAddr)


if __name__ == '__main__'
	patientDetails();
