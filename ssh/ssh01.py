# import getpass & netmiko

import getpass
from netmiko import ConnectHandler

# define devices
devices = {
    'device_type':'cisco_ios',
    'ip':'192.168.119.129',
    'username':'admin',
    'password':'cisco',
    'secret':'cisco'
}

# define log in details
devices['ip'] = input('Input IP address: ')
devices['username'] = input('Input Username: ')
devices['password'] = getpass.getpass('Input Password: ')
devices['secret'] = getpass.getpass('Input Secret: ')

print(devices)

# define SSH connection to remote node
ssh_connect = Connecthandler(**devices)
print('SSH connected successfully')

# enter enable mode
ssh_connect.enable()

# return current mode
print(ssh_connect.find_prompt())

# send commands to node
out = ssh_connect.send_command('show ip int b | ex un ')
print(out)

# send multiple commands to node using a list
cmd_list = ['interface loopback 0', 'ip add 1.1.1.1 255.255.255.255', 'end', 'write']
out = ssh_connect.send_config_set(cmd_list)
print(out)

ssh_connect.disconnect()
