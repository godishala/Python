#!/usr/bin/env python3

# using multiple commands with command names in  output

import paramiko
from getpass import getpass
import time
try:
    host = "192.168.88.138"
    username = "user" 
    cmd1 = ['ls /','systemctl status sshd --no-pager','whoami','hostname']

    session = paramiko.SSHClient()

    session.load_system_host_keys()
    
    # key containing passphrase
    #key_pass='1234'
    #key_file=paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_01',password=key_pass)
    key_file=paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_rsa'
    print(f"\n{'#'*50}\nConnecting to the Device {host} \n{'#'*50}")
    session.connect(hostname=host,
                    username=username,
                    pkey=key_file,
                    allow_agent=False,
                    look_for_keys=False,
                    port=22)



    DEVICE_ACCESS = session.invoke_shell()
    for command in cmd1:
        DEVICE_ACCESS.send(f'{command}\n')
        time.sleep(3)
        output = DEVICE_ACCESS.recv(650008008)
        print(output.decode(),end='')
    session.close()

except paramiko.ssh_exception.PasswordRequiredException:
    print("Required passphrase for private key")

except paramiko.ssh_exception.AuthenticationException:
    print("Please add the pub key to remote server")

# w.r.t exceptions in this script first it will check for passphrase exception if passphrase is present in key and not provided for pkey. if provided then it will check for public key availability in remote server
