#!/usr/bin/env python3

# using multiple commands with command names in  output

import paramiko
from getpass import getpass
import time
try:
    host = "192.168.88.138"
    username = "user" 
    print(f"Username is {username}")

    session = paramiko.SSHClient()

    session.load_system_host_keys()

    # this key must not contain the passphrase
    key_file=paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_03')
    session.connect(hostname=host,
                    username=username,
                    pkey=key_file,
                    allow_agent=False,
                    look_for_keys=False,
                    port=22)

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

except paramiko.ssh_exception.AuthenticationException:
    print("Please add the public key to remote server")

