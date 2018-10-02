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
script name   : thingspeak_cloud_data_read_display.py
Functionality : Read the thingspeak cloud data and display on the console
Created on    : 21 AUG 2016
"""

# Global imports
import urllib.request
import urllib.parse,json

#Global variables
READ_API_KEY='XXXXXXXXXXXXXXXXXXXXXXX'             # Desired channel Read api key to read the data
CHANNEL_ID=XXXXXXXX                                # Desired channel ID to read the data


def main():
    """
    Function name : main
    Parameter     : None
    Functionality : Function Reads the garbage level frop thr cloud and display in the console based on the given read api key
    Return Value  : None
    """
    try:
        while True:   
            conn = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                                       % (CHANNEL_ID, READ_API_KEY))
            response = conn.read()
            encoding = conn.info().get_content_charset('utf-8')
            data = json.loads(response.decode(encoding))
            print("")
            print ("Garbage System Data")
            level=data['field1']
            print ("Garbage Level:",level)
            bin_id=data['field2']
            print("Bin identity Number:",bin_id)
            bin_location=data['field3']
            print ("Bin Location:",bin_location)
            conn.close()
    except Exception as e_obj:
        print 'EXCEPTION: In main() %s' % e_obj


if __name__ == '__main__':
    main()
