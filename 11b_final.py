from netmiko import ConnectHandler

host1 = {
    'device_type': 'cisco_ios',
    'ip': '10.X.0.1',
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
    net_connect = ConnectHandler(**target)

    config_commands = ['int loop 11', 'ip address 11.1.1.X 255.255.255.0']

    output = net_connect.send_config_set(config_commands)
    print (output)

    output = net_connect.send_command('show ip int brief')
    print (output)
    print ("="*80)

    net_connect.disconnect()
