#!/usr/bin/env python
# coding=utf-8
from UCAS import UCAS
import numpy as np
class CreatAllId(UCAS):
    @classmethod
    def run(self):
        Sb = ['2', '1']
        Year = ['2013', '2014', '2015','2016']
        Dw = [str(i) for i in np.loadtxt('./data/danwei.txt', dtype=np.int32)]
        Xk = ['%02d' % i for i in np.arange(1, 51)]
        xxx = ['%03d' % i for i in np.arange(1, 10)]
        userID = [
            i +
            j +
            k +
            h +
            g for j in Sb for i in Year for g in xxx for h in Xk for k in Dw]
        userID = np.array(userID)
        np.save('./data/ALLid.npy',userID)
        print 'creat ALLid ......'
if __name__ == '__main__':
#   f=CreatAllId.run()
#   f.run()
    #or
    CreatAllId.run()

