#!/usr/bin/env python
# coding=utf-8
from UCAS import UCAS
import numpy as np
class CreatAllId(UCAS):
    @classmethod
    def run(self):
        Sb = ['2', '1']
        Year = ['2013', '2014', '2015']
        Dw = [str(i) for i in np.loadtxt('./data/danwei.txt', dtype=np.int32)]
        Xk = ['%02d' % i for i in np.arange(1, 51)]
        xxx = ['%03d' % i for i in np.arange(1, 2)]
        userID = [
            i +
            j +
            k +
            h +
            g for j in Sb for i in Year for g in xxx for h in Xk for k in Dw]
        userID = np.array(userID)
        np.save('./data/ALLid.npy',userID)
        print 'creat ALLid ......'
    def run_Valid_accounts(self):
        with open('./Valid_accounts.txt','r') as f:
            ID=f.readlines()
            f.close()
        ID=[i[:-1] for i in ID]
        ids=np.array([i[:-3]+'%03d'%num for i in ID for num in np.arange(2,50) ])
        np.save('./data/ALLid.npy',ids)

if __name__ == '__main__':
    f=CreatAllId()
    f.run_Valid_accounts()
    #or
#   CreatAllId.run()

