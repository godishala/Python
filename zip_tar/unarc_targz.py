#!/usr/bin/env python3
import os,tarfile

arc_name=os.path.expanduser(os.path.join('~','junk/work1.tar.gz'))
base_dir=os.path.dirname(arc_name)
os.chdir(base_dir)
tar=tarfile.open(arc_name,'r:gz')
tar.extractall()
tar.close()
script_path=os.path.realpath(__file__)
script_dir=os.path.dirname(script_path)
os.chdir(script_dir)
#print(script_dir)


