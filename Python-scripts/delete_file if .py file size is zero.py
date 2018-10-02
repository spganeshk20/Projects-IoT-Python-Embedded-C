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
script name   : delete_file_if_.py_file_size_is_zero.py
Functionality : Deletes the .py(python) file from the directory if .py(python) file size is zero
Created on    : 21 NOV 2015
"""

__author__ = 'Ganesh'

# Global import
import os

cwd = os.getcwd()
print cwd

count = 0
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.py') :
           count = count + 1
print 'Files:', count
i=1
a=[]
b=[]
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.py') :
           thefile = os.path.join(dirname,filename)
           a.append(thefile)
           b.append(os.path.getsize(thefile))
for i in range(len(a)):
    print a[i],b[i]
    if b[i]==0:
        os.remove(a[i])