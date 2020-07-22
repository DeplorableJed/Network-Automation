#!/usr/bin/env python3


# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems

import sys
sys.path.insert(0,'..') #This allows one directory back to be searched for imported objects
import json
import utils 
import dnac_apis #This is python script
import service_now_apis #This is python script
import os
import os.path
import difflib
import datetime

import requests
import urllib3
from requests.auth import HTTPBasicAuth  # for Basic Auth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

from config import DNAC_URL, DNAC_PASS, DNAC_USER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def compare_configs(cfg1, cfg2):
    """
    This function, using the unified diff function, will compare two config files and identify the changes.
    '+' or '-' will be prepended in front of the lines with changes
    :param cfg1: old configuration file path and filename
    :param cfg2: new configuration file path and filename
    :return: text with the configuration lines that changed. The return will include the configuration for the sections
    that include the changes
    """

    # open the old and new configuration fiels
    f1 = open(cfg1, 'r')
    old_cfg = f1.readlines()
    f1.close

    f2 = open(cfg2, 'r')
    new_cfg = f2.readlines()
    f2.close

    # compare the two specified config files {cfg1} and {cfg2}
    d = difflib.unified_diff(old_cfg, new_cfg, n=9)

    # create a diff_list that will include all the lines that changed
    # create a diff_output string that will collect the generator output from the unified_diff function
    diff_list = []
    diff_output = ''

    for line in d:
        diff_output += line
        if line.find('Current configuration') == -1:
            if line.find('Last configuration change') == -1:
                if (line.find('+++') == -1) and (line.find('---') == -1):
                    if (line.find('-!') == -1) and (line.find('+!') == -1):
                        if line.startswith('+'):
                            diff_list.append('\n' + line)
                        elif line.startswith('-'):
                            diff_list.append('\n' + line)

    # process the diff_output to select only the sections between '!' characters for the sections that changed,
    # replace the empty '+' or '-' lines with space
    diff_output = diff_output.replace('+!', '!')
    diff_output = diff_output.replace('-!', '!')
    diff_output_list = diff_output.split('!')

    all_changes = []

    for changes in diff_list:
        for config_changes in diff_output_list:
            if changes in config_changes:
                if config_changes not in all_changes:
                    all_changes.append(config_changes)

    # create a config_text string with all the sections that include changes
    config_text = ''
    for items in all_changes:
        config_text += items

    return config_text


def main():
    """
    This script will monitor device configuration changes. It could be executed on demand as in this lab, or periodically,
    every 60 minutes (for example). It will collect the configuration file for each device, compare with the existing cached file,
    detect if any changes.
    When changes detected, identify the last user that configured the device, and create a new ServiceNoe incident.
    """

    # get the DNA C auth token
    dnac_token = dnac_apis.get_dnac_jwt_token(DNAC_AUTH)
    print('\nDNA C AUTH TOKEN: ', dnac_token, '\n')

    temp_run_config = 'temp_run_config.txt'

    # get the DNA C managed devices list (excluded wireless)
    all_devices_info = dnac_apis.get_all_device_info(dnac_token)
    all_devices_hostnames = []
    for device in all_devices_info:
        if device['family'] == 'Switches and Hubs' or device['family'] == 'Routers':
            all_devices_hostnames.append(device['hostname'])

    # get the config files, compare with existing (if one existing). Save new config if file not existing.
    for device in all_devices_hostnames:
        device_run_config = dnac_apis.get_output_command_runner('show running-config', device, dnac_token)
        filename = str(device) + '_run_config.txt'

        # save the running config to a temp file

        f_temp = open(temp_run_config, 'w')
        f_temp.write(device_run_config)
        f_temp.seek(0)  # reset the file pointer to 0
        f_temp.close


        # check if device has an existing configuration file (to account for newly discovered DNA C devices)
        # if yes, run the diff function
        # if not, save the device configuration to the local device database

        if os.path.isfile(filename):
            diff = compare_configs(filename, temp_run_config)
            if diff != '':

                # retrieve the device location using DNA C REST APIs
                location = dnac_apis.get_device_location(device, dnac_token)

                # find the users that made configuration changes
                with open(temp_run_config, 'r') as f:
                    user_info = 'User info no available'
                    for line in f:
                        if 'Last configuration change' in line:
                            user_info = line

                # get the device management IP address
                device_mngmnt_ip_address = dnac_apis.get_device_management_ip(device, dnac_token)

                # define the incident description and comment
                short_description = "Configuration Change Alert"
                comment = "The device with the name: " + device + "\nhas detected a Configuration Change"
                comment += "\n\nThe device location is: " + location
                comment += "\n\nThe device management IP address is: " + device_mngmnt_ip_address
                comment += "\n\nThe configuration changes are\n" + diff + "\n\n" + user_info

                print(comment)

                # create ServiceNow incident using ServiceNow APIs
                incident = service_now_apis.create_incident(short_description, comment, SNOW_DEV, 3)
            else:
                print('Device: ' + device + ' - No configuration changes detected')

        else:
            f_config = open(filename, "w")
            f_config.write(device_run_config)
            f_config.seek(0)
            f_config.close


if __name__ == '__main__':
    main()
