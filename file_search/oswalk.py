#!/usr/bin/env python

import os
path="/home/user/pyt"

print('-------------------------')
for p,d,f in os.walk(path):
    if len(f) !=0:
       #print(p)
       #print(f)
       print(p)
       for each_file in f:
           #print(each_file)
           print(os.path.join(p,each_file))
       print("---------------------")

