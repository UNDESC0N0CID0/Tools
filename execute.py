import os
from os import listdir
from os.path import isfile, join
import subprocess

def ls(ruta = '.'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]
foo = ls()
foo.remove(os.path.basename(__file__))
for path in foo:
  process=[]
  process.append(subprocess.Popen(['py', f'{path}']))
  
