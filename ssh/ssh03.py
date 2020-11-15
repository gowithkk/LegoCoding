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

# def read command
def read_cmd(config_file):
    with open(config_file) as configfile:
        config_set = configfile.read()
        config_set = config_set.split('\n')
    return config_set

# def save config
def save_config(out):
    filename = devices['ip'] + '.txt'
    with open(filename, 'w+') as filen:
        filen.write(out)

# def SSH and configure
def ssh_config():
    # SSH into devices using ConnectHandler
    ssh_connect = ConnectHandler(**devices)
    print('SSH\'d in', devices['ip'])

    # enter enable mode
    ssh_connect.enable()

    # return current mode
    print(ssh_connect.find_prompt())
    time.sleep(2)
    print('Configuring...')

    # call def read_cmd to get config file
    file_name = input('Enter file name: ')
    config_set = read_cmd(file_name)

    # send commands to node
    out = ssh_connect.send_config_set(config_set)
    print(out)

    # save config into a file called filename
    save_config(out)

    # disconnect SSH
    ssh_connect.disconnect()


# read device list from a file
def read_ip_config(ip_file_name):
    with open(ip_file_name) as ip_file:
        print('Reading IP addresses, username, and password...')

        # SSH into devices mentioned in file ip_file
        for line in ip_file:
            ip_list = line.strip("\n").split(' ')
            devices['ip'] = ip_list[0]
            devices['username'] = ip_list[1]
            devices['password'] = ip_list[2]
            devices['secret'] = ip_list[3]
            print("\n\n Connecting: ", devices['ip'])

            # call def ssh_config
            ssh_config()
            print('Device {} complete!'.format(devices['ip']))

if __name__ == '__main__':
    ip_file_name = input('Type name of the IP list: ')
    read_ip_config(ip_file_name)