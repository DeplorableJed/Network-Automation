#!/usr/bin/env python3


# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems

import sys
sys.path.insert(0,'..') #This allows one directory back to be searched for imported objects
import json
import utils
import inspect
import requests
import urllib3
from requests.auth import HTTPBasicAuth  # for Basic Auth 
from urllib3.exceptions import InsecureRequestWarning  # To ignore insecure https warnings
from pprint import pprint
from config import DNAC_URL, DNAC_PASS, DNAC_USER #imports the config file one level back and imports 3 variables

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS) #Creates the Base64 encoded value
DEBUG=True

def get_dnac_jwt_token(dnac_auth):
    """
    Create the authorization token required to access DNA C
    Call to DNA C - /api/system/v1/auth/login
    :param dnac_auth - DNA C Basic Auth string
    :return: DNA C JWT token
    """
    log("Executing Function: "+inspect.stack()[0][3]) #Extracts the name of the function from memory and prints
    url = DNAC_URL + '/api/system/v1/auth/login'
    header = {'content-type': 'application/json'}
    response = requests.get(url, auth=dnac_auth, headers=header, verify=False)
    response_header = response.headers
    dnac_jwt_token = response_header['Set-Cookie'] #Gets the token value from the Set-Cookie key
    return dnac_jwt_token #Passes the token back to the script that ran the function

def get_client_info(client_ip, dnac_jwt_token):
    """
    This function will retrieve all the information from the client with the IP address
    :param client_ip: client IPv4 address
    :param dnac_jwt_token: DNA C token
    :return: client info, or {None} if client does not found
    """
    log("Executing Function: "+inspect.stack()[0][3])
    url = DNAC_URL + '/dna/intent/api/v1/network-device?managementIpAddress=' + client_ip
    header = {'content-type': 'application/json', 'Cookie': dnac_jwt_token}
    response = requests.get(url, headers=header, verify=False)
    client_json = response.json()
    try:
        client_info = client_json['response'][0]
        return client_info
    except:
        return None
def log(s):
    if DEBUG:
        print(s)

# get the DNA Center JWT auth

dnac_jwt_auth = get_dnac_jwt_token(DNAC_AUTH)
print('The DNA Center Auth JWT is: ', dnac_jwt_auth)
print('-'*80)
print()

# get the client info

client_ip_add = '1.1.1.1' #Replace with any provisioned device in DNAC
client_detail = get_client_info(client_ip_add, dnac_jwt_auth)
print('The information for the client with the IP address: ', client_ip_add)
pprint(client_detail)

