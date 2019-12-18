#!/usr/bin/python

from ansible.module_utils.basic import *
import requests
import urllib3

serveraddress = "1.4.28.28"
username = "admin"
password = "admin"
systemip = "172.1.30.3"

def initalize_connection(serveraddress,username,password):

    """
    This function will initialize a connection to thevManage
    :param ipaddress: This is the IP Address and Port number of vManage 
    :param username:  This is the username for vManage (admin in our lab)
    :param password:  This is a password for vManage (admin in our lab)
    These will be set in a file called package_config.ini
    """

    # Disable warnings like unsigned certificates, etc.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url="https://"+serveraddress+"/j_security_check"

    payload = "j_username="+username+"&j_password="+password
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        }

    sess=requests.session()

    # Handle exceptions if we cannot connect to the vManage
    try:
        response = sess.request("POST", url, data=payload, headers=headers,verify=False,timeout=10)
    except requests.exceptions.ConnectionError:
        print ("Unable to Connect to "+ipaddress)
        return False

    return sess

def get_inventory(serveraddress,session):

    module = AnsibleModule(argument_spec={})

    url = "https://" + serveraddress + "/dataservice/device"
    response = session.request("GET",url,verify=False,timeout=10)
    json_string = response.json()
    module.exit_json(changed=False, meta=json_string) 


session=initalize_connection(serveraddress,username,password)
if session != False:
    get_inventory(serveraddress,session)
