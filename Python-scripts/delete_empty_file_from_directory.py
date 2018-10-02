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
script name   : delete_empty_file_from_directory.py
Functionality : Deletes the empty file from the directory
Created on    : 21 NOV 2015
"""

__author__ = 'Ganesh'

# Global import
import os


cwd = os.getcwd()

count = 0
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.txt') :
           count = count + 1
print 'Files:', count
i=1
a,b=[], []
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.txt') :
           thefile = os.path.join(dirname,filename)
           a.append(thefile)
           b.append(os.path.getsize(thefile))
count1=1
for i in range(len(a)):
    print a[i],b[i]
    for i in range(len(a)):
        count1=0  
        for j in range(len(b)):
            if (a[i].endswith('.py') == a[j].endswith('.py')) & ((b[i]==0)&b[j]==0):
                count1=count1+1
    print count1
              
    if (count1>1):
        for k in range(1,count1):
            if((count1==k)):
                break
            else:
                os.remove(a[k])