#!/usr/bin/env python3

import socket

socket.setdefaulttimeout(.5)
print('\n'+'#' *50+'\n Started Executing Script from :'+socket.gethostname()+'\n'+'#'*50)

def scan_port(ip,port):
    print('-'*20)
    print('FQDN is: ' +socket.getfqdn(ip))
    try:
        print('IP is : '+socket.gethostbyname(ip))
    except:
        print('Exception Occured while getting ip')
        pass
    try:
        Device_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result_of_check = Device_Socket.connect_ex((ip,port))

        if result_of_check == 0:
            print(f"{ip} Listening on Port: {port}")
            Device_Socket.close()
        else:
            print(f"{ip} is not listening on port: {port}")
            Device_Socket.close()
    except socket.gaierror:
        print("could not resolve host: "+ ip)
    except:
        print("Exception Occured")

scan_port('192.168.88.138',22)
scan_port('qei',22)
scan_port('example',443)

print('\n Stopped Executing Script\n')

