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
script name   : app.py
Functionality : Turn ON/OFF the Led along with the intruder distance
Created on    : 19 JAN 2019
"""

# Global Imports
import time
import RPi.GPIO as gpio

# Local Imports
from utils import lib_utils as utils
from lib_cloud import cloud
from config import lib_config as config

# Global variable
BOOLEAN_RANGE_FINDER = False

# Mode initialization
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# Pin setup
gpio.setup(config.PIR_SENSOR_DIGITAL_OUTPUT_PIN, gpio.IN)
gpio.setup(config.LED_PIN, gpio.OUT)
gpio.setup(config.ULTRASONIC_SENSOR_ECHO_PIN, gpio.IN)
gpio.setup(config.ULTRASONIC_SENSOR_TRIGGER_PIN, gpio.OUT)


def range_finder(range_find):
    """
    Function name    : range_finder
    Functionality    : Finds the intruder distance
    Function Invoked : print_msg()
    Return value     : Returns True and distance in cm, otherwise False, None
    """
    try:
        pulse_start = 0
        pulse_end = 0
        if range_find is True:
            utils.print_msg("Measuring the Intruder distance")
            gpio.output(config.ULTRASONIC_SENSOR_TRIGGER_PIN, False)		# Set port/pin value to 0/GPIO.LOW/False
            time.sleep(config.NUMERIC_CONSTANT_TWO)			        # Waiting time For Sensor To Settle
            gpio.output(config.ULTRASONIC_SENSOR_TRIGGER_PIN, True)		# Set port/pin value to 1/GPIO.HIGH/True
            time.sleep(config.NUMERIC_CONSTANT_ONE/10000)
            gpio.output(config.ULTRASONIC_SENSOR_TRIGGER_PIN, False)
            while gpio.input(config.ULTRASONIC_SENSOR_ECHO_PIN) == \
                    config.NUMERIC_CONSTANT_ZERO:
                pulse_start = time.time()
            while gpio.input(config.ULTRASONIC_SENSOR_ECHO_PIN) == \
                    config.NUMERIC_CONSTANT_ONE:
                pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            distance_in_cm = pulse_duration * 17150                             # The speed of sound at sea level is 34300 cm/s
                                                                                # Hence the formula is 34300 * (time/2) = intruder_distance
            distance_in_cm = round(distance_in_cm, 2)
            utils.print_msg("Distance: %s cm" % distance_in_cm)
            return True, distance_in_cm
        else:
            utils.print_msg('Invalid range find parameter value. '
                            'Given range_find is %s' % range_find)
            return False, None
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In range_finder(), due to %s' % e_obj)
        return False, None


def main_execution():
    """
    Function name    : main_execution
    Functionality    : Checks the Intruder alert and finds its distance in cm
    Function Invoked : print_msg(), range_finder()
    Return value     : None
    """
    utils.print_msg('*' * config.NUMERIC_CONSTANT_SIXTY)
    utils.print_msg('\t\t\t\tIntruder Alert System')
    utils.print_msg('*' * config.NUMERIC_CONSTANT_SIXTY)
    try:
        while True:
            pir_sensor_digital_data = gpio.\
                input(config.PIR_SENSOR_DIGITAL_OUTPUT_PIN)
            if config.NUMERIC_CONSTANT_ONE == int(pir_sensor_digital_data):	    # Compare dynamic value with constants
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg("\tBreach Alert by Intruder")
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                gpio.output(config.LED_PIN, gpio.HIGH)
                utils.print_msg('LED Status: ON')
                utils.print_msg('Current Intruder status: %s'
                                % config.STR_BREACH)
                distance_in_cm, range_find_status = \
                    range_finder(BOOLEAN_RANGE_FINDER)
                cloud_write_status = cloud.cloud_data_write(config.STR_BREACH,
                                                            str(distance_in_cm))
                cloud_read_status = cloud.cloud_data_read(config.STR_RECENT)
            else:
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg("\tArea Under Safe")
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg('LED Status: OFF')
                utils.print_msg('Current Intruder status: %s' % config.STR_SAFE)
                gpio.output(config.LED_PIN, gpio.LOW)
                cloud_read_status = cloud.cloud_data_read(config.STR_LAST)
            system_rest_status_check = \
                cloud.system_reset_status_cloud_data_read()
            if config.NUMERIC_CONSTANT_ONE == system_rest_status_check:
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg("Intruder Alert System Force Restart")
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg("Updating the reset data information into cloud"
                                " server")
                cloud.cloud_data_write(config.STR_SAFE,
                                       config.NUMERIC_CONSTANT_ZERO)
                gpio.output(config.LED_PIN, gpio.LOW)
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg("System force reset")
                utils.print_msg(config.STR_SYMBOL *
                                config.NUMERIC_CONSTANT_THIRTY)
                utils.print_msg('LED Status: OFF')
                utils.print_msg('Current Intruder status: %s' % config.STR_SAFE)
                utils.print_msg(config.STR_SYMBOL_STAR *
                                config.NUMERIC_CONSTANT_EIGHTY)
            time.sleep(config.NUMERIC_CONSTANT_TEN)                             # Loop iterates once in every 10 seconds
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In main_execution(), due to %s' % e_obj)
    finally:
        gpio.cleanup()


# Execution begins here
if __name__ == '__main__':
    try:
        main_execution()
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: Fail to start the intruder alert '
                        'system. Due to %s' % e_obj)

