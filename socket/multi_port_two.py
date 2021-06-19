#!/usr/bin/env python3

import socket

socket.setdefaulttimeout(.5)
print('\n'+'#' *50+'\n Started Executing Script\n'+'#'*50)
def port_check(ip,port):
#destination = ('192.168.88.138',42)
    Device_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#result_of_check = Device_Socket.connect(destination)
#print(result_of_check)

# connect_ex will give the return status of connection
    result_of_check = Device_Socket.connect_ex((ip,port))
#print(result_of_check)

    if result_of_check == 0:
        print(f"{ip} Listening on Port: {port}")
        Device_Socket.close()
    else:
        print(f"{ip} is not listening on port: {port}")
        Device_Socket.close()

port_check('192.168.88.138',22)
port_check('192.168.88.138',443)

print('\n Stopped Executing Script\n')

