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
script name   : directory_analysis_appending_file_name_with_file_size.py
Functionality : Get the file name and file size details from directory
Created on    : 21 NOV 2015
"""

__author__ = 'Ganesh'

# Global import
import os

cwd = os.getcwd()
print cwd
listdir=os.listdir(cwd)
print listdir
path=os.path.abspath('ne.py')
print path
pathexist=os.path.exists('ne.py')
print pathexist
pathdir=os.path.isdir('ne.py')
print pathdir

count = 0													# Count the number of .py(any extension) file in particular directory
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.py') :
           count = count + 1
print 'Files:', count

from os.path import join									# To concatenate the file name and directory
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.py') :
           thefile = os.path.join(dirname,filename)
           print os.path.getsize(thefile), thefile