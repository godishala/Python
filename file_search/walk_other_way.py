#!/usr/bin/env python3
import os

path_provided=input("Enter the Name of Path : ")
file_extension=input("Enter the File Extension : ")
dir_structure=os.walk(path_provided)

for r,d,f in dir_structure:
    for file in f:
        if f != 0:
            if file.endswith(file_extension):
                print(os.path.join(r,file))
