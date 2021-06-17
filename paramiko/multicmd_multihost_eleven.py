#!/usr/bin/env python3

# using multiple commands with command names in  output

import paramiko
from getpass import getpass
import time
try:
    username = "user" 
    cmd1 = ['ls /',
            'systemctl status httpd --no-pager',
            'cat /etc/passwd | cut -d: -f 1,3',
            'hostname']

    session = paramiko.SSHClient()

    session.load_system_host_keys()
    
    # key containing passphrase
    #key_pass='1234'
    #key_file=paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_01',password=key_pass)
    key_file=paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_rsa')
    def linux_exec(host,cmd1):
        try:
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
        except:
            print("Unable to connect to device")

#except paramiko.ssh_exception.PasswordRequiredException:
#    print("Required passphrase for private key")

except paramiko.ssh_exception.AuthenticationException:
    print("Please add the pub key to remote server")

linux_exec("192.168.88.13",cmd1)
linux_exec("192.168.88.138",cmd1)
