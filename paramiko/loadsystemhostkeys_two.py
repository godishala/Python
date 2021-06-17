#!/usr/bin/env python3

import paramiko
from getpass import getpass
import time
try:
    host = "192.168.88.138"
    #username = (input("Enter Username : ") or "user")
    username = "user"
    print(f"Username is {username}")
    #password = getpass("Enter Password :")
    password = "user123"

    session = paramiko.SSHClient()
    #session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ### use load_system_host_keys only when the key of remote host is present in known_hosts
    session.load_system_host_keys()
    session.connect(hostname=host,username=username,password=password,port=22)

    stdin,stdout,stderr = session.exec_command('hostname')
    time.sleep(.5)
    print(f'Hostname is : {stdout.read().decode()}')
    session.close()
except  paramiko.ssh_exception.AuthenticationException:
    print("provide correct password")
#.ssh_exception.AuthenticationException:
