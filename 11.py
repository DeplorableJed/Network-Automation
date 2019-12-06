from netmiko import ConnectHandler

host1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.0.1',
    'username': 'Admin',
    'password': 'NterOne1!',
}


net_connect = ConnectHandler(**host)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 11', 'ip address 11.1.1.X 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output
