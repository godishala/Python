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
    password = "user"

    session = paramiko.SSHClient()
    #session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    ### use load_system_host_keys only when the key of remote host is present in known_hosts file in home directory
    #session.load_system_host_keys()

    ### use load_host_keys to load a particular known_hosts key file
    #session.load_host_keys('/home/user/.ssh/known_hosts')
    
    ### use RejectPolicy to reject the connection when there is no key in known_hosts file
    #session.set_missing_host_key_policy(paramiko.RejectPolicy)

    ### if there is already key in known_hosts file reject policy wont work, if the key does not exits in load_host_keys then reject policy will take effect
    #session.load_host_keys('/home/user/.ssh/known_hosts')
    #session.set_missing_host_key_policy(paramiko.RejectPolicy)


    ### for this even if key is not present in known_hosts server gives the warning and continues to login to host, if key is found in known_hosts no warning will be produced
    session.load_host_keys('/home/user/.ssh/known_hosts')
    session.set_missing_host_key_policy(paramiko.WarningPolicy)


    session.connect(hostname=host,username=username,password=password,port=22)



    stdin,stdout,stderr = session.exec_command('hostname')
    time.sleep(.5)
    print(f'Hostname is : {stdout.read().decode()}')
    session.close()
except  paramiko.ssh_exception.AuthenticationException:
    print("provide correct password")
