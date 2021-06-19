#!/usr/bin/env python3

import tarfile
import os

archive_file=os.path.expanduser(os.path.join('~','work1.tar.gz'))
#print(archive_file)
tar_file=tarfile.open(archive_file, 'r:gz')
print(type(tar_file))
print(tar_file.getnames())
