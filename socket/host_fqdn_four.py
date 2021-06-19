#!/usr/bin/env python3

import socket

socket.setdefaulttimeout(.5)
print('\n'+'#' *50+'\n Started Executing Script from :'+socket.gethostname()+'\n'+'#'*50)

def scan_range(ip,sp,ep):
    ep = ep+1
    print('\n'+'-'*10+' Scanning '+ip+'-'*10+'\n')
    print(socket.getfqdn(ip)+'\n')
    try:
        for port in range(sp,ep):
            Device_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result_of_check = Device_Socket.connect_ex((ip,port))

            if result_of_check == 0:
                print(f"{ip} Listening on Port: {port}")
                Device_Socket.close()
            else:
                print(f"{ip} is not listening on port: {port}")
                Device_Socket.close()
    except:
        print('Exception occured')

scan_range('192.168.88.138',1,25)
scan_range('192.168.88.137',1,25)

print('\n Stopped Executing Script\n')

