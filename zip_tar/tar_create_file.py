#!/usr/bin/env python3
import os
import tarfile

############for creating new tar archive
arc_file=os.path.expanduser(os.path.join('~','work2.tar'))
#print(arc_file)
tar_file=tarfile.open(arc_file,'w')
#for file in tar_file.getnames():
#    print(file)
#with out directories
dir_walk=os.walk('/home/user/Project')

for r,d,f in dir_walk:
    for file in f:
        if not file == 0 or file == '':
           dir_path=os.path.join(r,file)
           dir_name=os.path.dirname(dir_path)
        # perfectly done for only copying files without directories
           os.chdir(dir_name)
           #print(file)
        tar_file.add(file)
           
tar_file.close()


"""
# with directories
dir_walk=os.walk('/home/user/Project')
for r,d,f in dir_walk:
    for file in f:
        if not file == 0 or file == '':
           dir_path=os.path.join(r,file)
        tar_file.add(dir_path)
"""

'''
############################ for appending the files
arc_file=os.path.expanduser(os.path.join('~','work2.tar'))
#print(arc_file)
tar_file=tarfile.open(arc_file,'a')
#for file in tar_file.getnames():
#    print(file)
#with out directories
dir_walk=os.walk('/home/user/Project')

for r,d,f in dir_walk:
    for file in f:
        if not file == 0 or file == '':
           dir_path=os.path.join(r,file)
           dir_name=os.path.dirname(dir_path)
        # perfectly done for only copying files without directories
           os.chdir(dir_name)
           #print(file)
        tar_file.add(file)
           
tar_file.close()


# with directories
dir_walk=os.walk('/home/user/Project')
for r,d,f in dir_walk:
    for file in f:
        if not file == 0 or file == '':
           dir_path=os.path.join(r,file)
        tar_file.add(dir_path)


'''
