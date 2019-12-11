from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

host1 = {
    'device_type': 'cisco_ios',
    'ip': '10.X.0.17',
    'username': 'Admin',
    'password': 'NterOne1!',
}

host2 = {
    'device_type': 'cisco_ios',
    'ip': '10.X.1.2',
    'username': 'Admin',
    'password': 'NterOne1!',
}

host3 = {
    'device_type': 'cisco_ios',
    'ip': '10.X.3.3',
    'username': 'Admin',
    'password': 'NterOne1!',
}

routers =[host1, host2, host3]
for target in routers:
    try:
        net_connect = ConnectHandler(**target)
    except (AuthenticationException):
        print ('Authentication Failure: ' + str(target))
        continue
    except (NetMikoTimeoutException):
        print ("\n" + "*"*80)
        print ('Timeout to device: ' + str(target))
        print ("*"*80)
        continue
    except (SSHException):
        print ("\n" + "*"*80)
        print ('SSH might not be enabled: ' + str(target))
        print ("*"*80)
        continue
    except (EOFError):
        print ("\n" + "*"*80)
        print ('\n' + 'End of attempting device: ' + str(target))
        print ("*"*80)
        continue
    except (unknown_error):
        print ("\n" + "*"*80)
        print ('Some other error! ' + str(target))
        print ("*"*80)
        continue

    config_commands = ['int loop 11', 'ip address 11.1.1.X 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print (output)

    output = net_connect.send_command('show ip int brief')
    print (output)
    print ("="*80)

    net_connect.disconnect()
