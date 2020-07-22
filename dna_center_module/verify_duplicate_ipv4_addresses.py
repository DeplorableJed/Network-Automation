#!/usr/bin/env python3


# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems


import urllib3
from requests.auth import HTTPBasicAuth  # for Basic Auth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

import dnac_apis
import utils
from config import DNAC_PASS, DNAC_USER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def main():
    """
    - This script will:
      - load a file with a configuration to be deployed to a network device
      - identify the IPv4 addresses that will be configured on interfaces
      - search in the DNA Center database if these IPV4 addresses are configured on any interfaces
      - find if any clients are using the IPv4 addresses
    - Determine if deploying the configuration file will create an IP duplicate
    """

    # configuration template file name
    config_file = 'configuration_template.txt'

    # open file with the template
    cli_file = open(config_file, 'r')

    # read the file
    cli_config = cli_file.read()
    print('\n The CLI template:\n')
    print(cli_config)

    ipv4_address_list = utils.identify_ipv4_address(cli_config)
    print('\nThese valid IPv4 addresses will be configured:\n')
    print(ipv4_address_list)

    # get the DNA Center Auth token

    dnac_token = dnac_apis.get_dnac_jwt_token(DNAC_AUTH)
    print('\nThe DNA Center token is: ', dnac_token, '\n')

    # check each address against network devices and clients database
    # initialize duplicate_ip

    duplicate_ip = False
    for ipv4_address in ipv4_address_list:

        # check against network devices interfaces

        try:
            device_info = dnac_apis.check_ipv4_network_interface(ipv4_address, dnac_token)
            duplicate_ip = True
            if len(device_info) == 2:
                print('The IPv4 address ', ipv4_address, ' is used on this device ', device_info[0], ' interface ', device_info[1])
            else:
                print('The IPv4 address ', ipv4_address, ' is used on this device ', device_info[0])
        except:
            pass

        # check against any hosts

        try:
            client_info = dnac_apis.get_client_info(ipv4_address, dnac_token)
            if client_info is not None:
                duplicate_ip = True
                print('The IPv4 address ', ipv4_address, ' is used by a client')
        except:
            pass

    if duplicate_ip:
        print('\nDeploying the template ', config_file, ' will create IP duplicates')
    else:
        print('\nDeploying the template ', config_file, ' will not create IP duplicates')

    # end of the application run

    print('\n\nEnd of Application Run')


if __name__ == '__main__':
    main()
