#!/usr/bin/env python
# coding=utf-8
import numpy as np
import time
from src.login import LogIn
from src.logout import logout
class Info():
    pass
info=Info()
info.log=''

f=open('./ucasID.txt','r')
f.readline()
r=f.readlines()
ID=[]
Passwd=[]

f=LogIn()
for i in np.arange(len(r)):
    ID.append(r[i].split('\t')[0])
    Passwd.append(r[i].split('\t')[1][:-1])
print ID
print Passwd

# random selection:
def rand_sel():
    sampling=int(np.random.rand()*len(r))
    userid=ID[sampling]
    userpasswd=Passwd[sampling]
    return userid, userpasswd

def login_loop(Nloop=100):
    NumLoop=0
    print info.log
    while info.log!= 'success':
        time.sleep(1)
        username , pwd= rand_sel()
        info.log=f.run(username=username, pwd=pwd)
        NumLoop+=1
        if NumLoop>Nloop:
            break
    if info.log == 'success':
        time.sleep(3600)
        logout()
        info.log=''

while True:
    login_loop()

