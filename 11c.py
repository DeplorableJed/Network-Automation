from netmiko import ConnectHandler

host1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.0.1',
    'username': 'Admin',
    'password': 'NterOne1!',
}

host2 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.2',
    'username': 'Admin',
    'password': 'NterOne1!',
}

host3 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.3.3',
    'username': 'Admin',
    'password': 'NterOne1!',
}

routers =[host1, host2, host3]
for target in routers:
    try:
        net_connect = ConnectHandler(**target)
    except (AuthenticationException):
        print ('Authentication Failure: ' + ip)
        continue
    except (NetMikoTimeoutException):
        print ('\n' + 'Timeout to device: ' + ip)
        continue
    except (SSHException):
        print ('SSH might not be enabled: ' + ip)
        continue
    except (EOFError):
        print ('\n' + 'End of attempting device: '  ip)
        continue
    except unknown_error:
        print ('Some other error: ' + str(unknown_error))
        continue

    output = net_connect.send_command('show ip int brief')
    print output

    net_connect.disconnect()
