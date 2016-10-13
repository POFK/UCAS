#!/usr/bin/env python
# coding=utf-8
def read(path='./parameter'):
    f=open(path,'r')
    par=f.readlines()
    f.close()
    Par={}
    for i in par:
        x=i.replace(' ','').replace('\n','').split(':')
        Par[x[0]]=x[1]
    Par['NumberToRun']=int(Par['NumberToRun'])
    Par['CreatAllId']=Par['CreatAllId']=='True'
    print Par
    return Par
if __name__=='__main__':
    print read()

