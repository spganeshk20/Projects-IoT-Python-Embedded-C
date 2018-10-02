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
script name   : garbage_data_collector.py
Functionality : Writes the garbage current level data into thingspeak cloud
Created on    : 21 AUG 2016
"""

# Global imports
import time
import http.client, urllib.parse

# Global variaables
bin_location = "1st cross,whitefield"


def cloud_data_update(msg, channel_write_api_key, bin_id=1):
    """
    Function name : cloud_data_update
    Parameter     : msg, channel_write_api_key, bin_id
    Functionality : Writes the data into cloud based on the given channel write api key
    Return Value  : None
    """
    try:
        params = urllib.parse.urlencode({'field1':msg,'field2':bin_id,'field3':bin_location,'key': channel_write_api_key})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e_obj
        print 'EXCEPTION: In cloud_data_update() %s' % e_obj


def main():
    """
    Function name : main
    Parameter     : None
    Functionality : Function monitors the garbage level remotely
    Return Value  : None
    """
    try:
        for level in range(9):
            if(i%2==0):
                cloud_data_update_check = cloud_data_update(level, channel_write_api_key)   # Channel 1 write api key
                if cloud_data_update_check is True:
                    print 'Cloud data write succcessful'
                else:
                    print 'Cloud data write unsuccessful. \
                           Returned value from cloud_data_update() is %s ' % cloud_data_update_check
                
            if(level==0):
                cloud_data_update("Initial Bin level", channel_write_api_key)               # Channel 2 write api key
            elif(level==6):
                cloud_data_update("3/4 of bin was filled", channel_write_api_key)           # Channel 2 write api key
            elif(level==8):
                cloud_data_update("Bin filled and spilling out", channel_write_api_key)     # Channel 2 write api key
            time.sleep(20)
    except Exception as e_obj:
        print 'EXCEPTION: In main() %s' % e_obj


if __name__ == '__main__':
    main()
