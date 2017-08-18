#!/usr/bin/env python
# coding=utf-8
import numpy as np
f=open('./ucasID.txt','r')
f.readline()
r=f.readlines()
ID=[]
Passwd=[]
for i in np.arange(len(r)):
    ID.append(r[i].split('\t')[0])
    Passwd.append(r[i].split('\t')[1][:-1])
# random selection:
sampling=int(np.random.rand()*len(r))
userid=ID[sampling]
userpasswd=Passwd[sampling]
from src.login import LogIn
username =  userid
pwd = userpasswd
f=LogIn()
print f.run(username=username, pwd=pwd)
