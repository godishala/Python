#!/usr/bin/env python3

# using multiple commands with command names in  output

import paramiko
from getpass import getpass
import time
host = "192.168.88.138"
username = "user"
print(f"Username is {username}")
password = "user123"

session = paramiko.SSHClient()

session.load_system_host_keys()
session.connect(hostname=host,username=username,password=password,port=22)

commands = ['ls /', 'echo $USER','hostname','sdfgh']
#banner = '#' * 10

for command in commands:

    #print("{} Executing the command: {} {}".format(banner,command,banner))
    #print(f'{banner} Executing the command : {command} {banner}')
    print(f'{"#"*10} Executing the command : {command} {"#"*10}')
    stdin,stdout,stderr = session.exec_command(command)
    time.sleep(.5)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err: 
        print(err)
session.close()
