#!/usr/bin/python2.7

"""
------------------------------------------
        License Information
------------------------------------------
        GNU GENERAL PUBLIC LICENSE
        Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc
https://fsf.org/ Everyone is permitted to copy and
distribute verbatim copies of this license document,
but changing it is not allowed.
Note: For detailed license information,
please read the LICENSE file in the repository
[Repository Name: Projects-IoT-Python-Embedded-C]
"""

__author__ = 'Ganesh'

"""
script name   : web_app.py
Functionality : Flask application to display the data on Intruder System
                Dashboard
Created on    : 20 JAN 2019
"""

# Global Imports
from flask import Flask, render_template, redirect, url_for

# Local Imports
from lib_cloud import cloud
from config import lib_config as config
from utils import lib_utils as utils

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        temp_last_distance_data = 0
        while True:
            cloud_read_status, data = \
                cloud.cloud_read(config.DATA_CHANNEL_ID,
                                 config.DATA_CHANNEL_READ_API_KEY)
            if cloud_read_status is True:
                utils.print_msg(data)
            system_cloud_read_status, system_data = \
                cloud.cloud_read(config.SYSTEM_CHANNEL_ID,
                                 config.SYSTEM_CHANNEL_READ_API_KEY)
            if system_cloud_read_status is True:
                utils.print_msg(data)

            if temp_last_distance_data != data['field3']:
                return render_template('home.html',
                                       data_value=data,
                                       system_value=system_data)
            else:
                return redirect(url_for('index'))
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In index(), due to %s' % e_obj)
        return redirect(url_for('index'))


@app.route("/system_reset", methods=['GET', 'POST'])
def system_reset():
    try:
        cloud.system_reset_status_cloud_data_write(1)
        return redirect(url_for('index'))
    except Exception as e_obj:
        utils.print_msg('EXCEPTION: In system_reset(), due to %s' % e_obj)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)


