#!/usr/bin/env python3
import os
path="/etc"

for p,d,f in os.walk(path):
    if len(f) != 0:
       print(p)
       for each_file in f:
           print(os.path.join(p,each_file))
       print('----------------')
       
       


