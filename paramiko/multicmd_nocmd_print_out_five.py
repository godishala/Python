#!/usr/bin/env python3

# using multiple commands without having commands in output

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

for command in commands:

    stdin,stdout,stderr = session.exec_command(command)
    time.sleep(.5)
    print(stdout.read().decode())
print(stderr.read().decode())
session.close()
