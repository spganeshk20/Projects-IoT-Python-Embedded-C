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
please read the LICENSE file in the repository
[Repository Name: Projects-IoT-Python-Embedded-C]
"""

__author__ = 'Ganesh'

"""
script name   : cloud.py
Functionality : Writes the data into thingspeak cloud
Created on    : 20 JAN 2019
"""

# Global Imports
import time
import json
import httplib
import urllib
import datetime

# Local Imports
from utils import lib_utils as utils
from config import lib_config as config


def cloud_write(msg_or_system_reset_status, distance_in_cm, write_api_key,
                signal):
    """
    Function name    : cloud_write
    Parameter        : msg_or_system_reset_status, distance_in_cm,
                       write_api_key, signal
    Functionality    : Writes the data into cloud server
    Function Invoked : utils.print_msg()
    Return Value     : Returns True and timestamp on success,
                       False and None on failure
    """
    conn = None
    try:
        timestamp = datetime.datetime.now()
        if str(signal).upper() == config.STR_DATA:
            params = urllib.urlencode({'field1': str(msg_or_system_reset_status),
                                       'field2': str(timestamp),
                                       'field3': str(distance_in_cm),
                                       'key': write_api_key})
        else:
            params = urllib.urlencode(
                {'field1': str(msg_or_system_reset_status),
                 'field2': str(timestamp),
                 'key': write_api_key})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        utils.print_msg('Writing the data into cloud....')
        time.sleep(30)
        utils.print_msg('Data written to the cloud successful')
        return True, timestamp
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In cloud_write(), due to %s' % e_obj)
        return False, None
    finally:
        conn.close()


def cloud_read(channel_id, read_api_key):
    """
    Function name    : cloud_read
    Parameter        : channel_id, read_api_key
    Functionality    : Reads the data from the cloud server
    Function Invoked : utils.print_msg()
    Return Value     : Returns True and data on Success,
                       False and None on failure
    """
    conn = None
    try:
        conn = urllib.urlopen("http://api.thingspeak.com/channels/%s/feeds/"
                              "last.json?api_key=%s"
                              % (channel_id, read_api_key))
        response = conn.read()
        data = json.loads(response)
        return True, data
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In cloud_read(), due to %s' % e_obj)
        return False, None
    finally:
        conn.close()


def cloud_data_write(msg=config.STR_NONE, distance_in_cm=config.STR_NONE):
    """
    Function name    : cloud_data_write
    Parameter        : msg, distance_in_cm
    Functionality    : Writes the data into cloud server
    Function Invoked : cloud_write(), utils.print_msg()
    Return Value     : Returns True on success, False on failure
    """
    try:
        cloud_write_status, timestamp = cloud_write(msg,
                                                    distance_in_cm,
                                                    config.
                                                    DATA_CHANNEL_WRITE_API_KEY,
                                                    config.STR_DATA)
        if cloud_write_status is True:
            return True
        else:
            utils.print_msg('Invalid data provided:'
                            '\nmsg - %s'
                            '\ntimestamp - %s'
                            '\ndistance in cm - %s'
                            % (msg, timestamp, distance_in_cm))
            return False
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In cloud_data_write(), due to %s' % e_obj)
        return False


def cloud_data_read(log_msg):
    """
    Function name    : cloud_data_read
    Parameter        : log_msg
    Functionality    : Writes the data into cloud server
    Function Invoked : utils.print_msg(), cloud_read()
    Return Value     : Returns True on Success and False on failure
    """
    try:
        cloud_read_status, data = \
            cloud_read(config.DATA_CHANNEL_ID, config.DATA_CHANNEL_READ_API_KEY)
        if cloud_read_status is True:
            utils.print_msg(config.STR_SYMBOL * config.NUMERIC_CONSTANT_FIFTEEN
                            + ' ' + log_msg +
                            " Intruder Breach Alert Information "
                            + config.STR_SYMBOL *
                            config.NUMERIC_CONSTANT_FIFTEEN)
            intruder_status_msg = data['field1']
            utils.print_msg("Intruder status: %s" % intruder_status_msg)        # Either safe or breach
            time_stamp = data['field2']
            utils.print_msg("Time Intruder detected: %s" % time_stamp)
            distance_in_cm = data['field3']
            utils.print_msg("Distance Intruder Identified: %s" % distance_in_cm)
            return True
        else:
            return False
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In cloud_data_read(), due to %s' % e_obj)
        return False


def system_reset_status_cloud_data_write(system_reset_status):
    """
    Function name    : system_reset_status_cloud_data_write
    Parameter        : system_reset_status
    Functionality    : Writes the system reset status cloud data server
    Function Invoked : utils.print_msg(), cloud_write()
    Return Value     : Returns True on success, False on failure
    """
    try:
        cloud_write_status, timestamp = cloud_write(system_reset_status,
                                                    config.STR_NONE,
                                                    config.
                                                    SYSTEM_CHANNEL_WRITE_API_KEY,
                                                    config.STR_SYSTEM)
        if cloud_write_status is True:
            return True
        else:
            utils.print_msg('Invalid data provided:'
                            '\nsystem_reset_status - %s'
                            '\nsystem_reset_time - %s'
                            % (system_reset_status, timestamp))
            return False
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In system_reset_status_cloud_data_write()'
                        ', due to %s' % e_obj)
        return False


def system_reset_status_cloud_data_read():
    """
    Function name : system_reset_status_cloud_data_read
    Parameter     : None
    Functionality : Reads the system reset status cloud data server
    Return Value  : Returns system_reset_status on success, False on failure
    """
    try:
        cloud_read_status, data = \
            cloud_read(config.SYSTEM_CHANNEL_ID,
                       config.SYSTEM_CHANNEL_READ_API_KEY)
        if cloud_read_status is True:
            utils.print_msg(config.STR_SYMBOL * config.NUMERIC_CONSTANT_FIFTEEN
                            + " Intruder Alert System Reset Status " +
                            config.STR_SYMBOL * config.NUMERIC_CONSTANT_FIFTEEN)
            system_reset_status = data['field1']
            if config.NUMERIC_CONSTANT_ONE == int(system_reset_status):
                system_reset_string = config.STR_ON
            else:
                system_reset_string = config.STR_OFF
            utils.print_msg("System reset status: %s" % system_reset_string)    # If value is 1, do reset
            last_system_reset_time = data['field2']
            utils.print_msg("Last System reset time: %s" %
                            last_system_reset_time)
            if config.STR_ON.lower() == str(system_reset_string).lower():
                utils.print_msg("Updating the reset system information into"
                                " cloud server")
                time.sleep(15)
                system_reset_status_check = \
                    system_reset_status_cloud_data_write(0)
                if system_reset_status_check is False:
                    return False
            utils.print_msg(config.STR_SYMBOL_STAR *
                            config.NUMERIC_CONSTANT_EIGHTY)
            return int(system_reset_status)
        else:
            return False
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In system_reset_status_cloud_data_read(), '
                        'due to %s' % e_obj)
        return False
