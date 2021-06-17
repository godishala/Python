#!/usr/bin/env python3
import os

path_input=input('Enter the Path : ')
file_input=input('Enter the file name : ')
dir_struct=os.walk(path_input)
for r,d,f in dir_struct:
    for file in f:
        if file != 0:
            if file == file_input:
                print(os.path.join(r,file))
