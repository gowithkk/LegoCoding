import getpass
from netmiko import ConnectHandler
import time

# define devices
devices = {
    'device_type':'cisco_ios',
    'ip':'192.168.119.129',
    'username':'admin',
    'password':'cisco',
    'secret':'cisco'
}

# read device list from a file
ip_file = open('ip_lists.txt')
print('Reading IP addresses, username, and password...')

# read config file
with open('config_file.txt') as configfile:
    config_set = configfile.read()
    config_set = config_set.split('\n')

# SSH into devices mentioned in file ip_file
for line in ip_file:
    ip_list = line.strip("\n").split(' ')
    devices['ip'] = ip_list[0]
    devices['username'] = ip_list[1]
    devices['password'] = ip_list[2]
    devices['secret'] = ip_list[3]
    print("\n\n Connecting: ", devices['ip'])

    # SSH into devices using ConnectHandler
    ssh_connect = ConnectHandler(**devices)
    print('SSH\'d in', devices['ip'])

    # enter enable mode
    ssh_connect.enable()

    # return current mode
    print(ssh_connect.find_prompt())
    time.sleep(2)
    print('Configuring...')

    # send commands to node
    out = ssh_connect.send_config_set(config_sent)
    print(out)

    # save config into a file called filename
    filename = devices['ip'] + '.txt'
    with open(filename, 'w+') as filen:
        filen.write(out)
    ssh_connect.disconnect()
    print('Device {} complete!'.format(devices['ip']))

ip_file.close()