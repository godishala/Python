#!/usr/bin/env python3

import socket

socket.setdefaulttimeout(.5)
print('\n Started Executing Script\n')

destination = ('192.168.88.138',42)
Device_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#result_of_check = Device_Socket.connect(destination)
#print(result_of_check)

# connect_ex will give the return status of connection
result_of_check = Device_Socket.connect_ex(destination)
#print(result_of_check)

if result_of_check == 0:
    print("Listening on Port")
    Device_Socket.close()
else:
    print("is not listening on port")
    Device_Socket.close()
