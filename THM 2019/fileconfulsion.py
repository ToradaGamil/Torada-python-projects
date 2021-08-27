import os
import shutil
from importlib.metadata import *
import zipfile
from time import sleep

if os.path.isdir('tmp'):
    shutil.rmtree('tmp')
    ls = os.listdir()
    for l in ls:
        tmp = l.split('.')
        if tmp[1]=='zip':
            with zipfile.ZipFile(l, 'r') as zip_ref:
                zip_ref.extractall('tmp')
else:
    ls = os.listdir()
    for l in ls:
        tmp = l.split('.')
        if tmp[1]=='zip':
            with zipfile.ZipFile(l, 'r') as zip_ref:
                zip_ref.extractall('tmp')
ls2 = os.listdir('tmp/')
sleep(1)
if os.path.isdir('tmp/text/'):
    shutil.rmtree('tmp/text/') #remove directory with content
for l in ls2:
    tmp2 = l.split('.')
    if tmp2[1] =='zip':
        with zipfile.ZipFile('tmp/'+l, 'r') as zip_ref:

            zip_ref.extractall("tmp/text")
ltext=os.listdir('tmp/text/')
print(len(ltext))

#with zipfile.ZipFile(sys.argv[1], 'r') as zip_ref:
    #zip_ref.extractall()
for l in ltext:
    print(os.name(l))
p = 'password'
for l in ltext:
    with open('tmp/text/'+l,'r') as reader:
        T=reader.readlines()
        for ll in T:
            nl = ll.strip('\n')
            if p in nl:
                print(ll+'\n'+l)
