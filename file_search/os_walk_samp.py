#!/usr/bin/env python3
import os

path_check=input('Enter the path : ')
if (os.path.exists(path_check)):
    if (os.path.isdir(path_check)):
        dir_struct=os.walk(path_check)
        for r,d,f in dir_struct:
            print("The Directory is : ",r)
            for file in f:
                if file !=0:
                    print(os.path.join(r,file))
        print("-------------")
    else:
        print("\nPlease provide the directory path instead of file path")

else:
    print("\nPlease provide the path which is existing, You have provided the path which doesnot exists")
