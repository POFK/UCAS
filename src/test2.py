#!/usr/bin/env python
# coding=utf-8
import httplib
import urllib
# ================================================================================
loginurl = 'http://210.77.16.21/eportal/InterFace.do?method=login'
#get Information:
def GetInfo():
    url_Info='http://210.77.16.21/eportal/InterFace.do?method=getOnlineUserInfo'
    # 定义一些文件头
    headers = {'Host': '210.77.16.21',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    # 与网站构建一个连接
    conn = httplib.HTTPConnection("210.77.16.21")
    # 开始进行数据提交   同时也可以使用get进行
    conn.request(method="GET", url=url_Info, headers=headers)
    # 返回处理后的数据
    response = conn.getresponse()
    res = response.read()
    par={}
    for i in res.split(','):
        if 'userIndex' in i:
            par['userIndex']=i.split('":')[1][1:-1]
        if 'maxFlow' in i:
            par['maxFlow']=i.split('":')[1][1:-1]
        if 'userName' in i:
            par['userName']=i.split('":')[1][1:-1]
        if '"password"' in i:
            par['password']=i.split('":')[1][1:-1]
        if 'userId' in i:
            par['userId']=i.split('":')[1][1:-1]
        if 'userMac' in i:
            par['userMac']=i.split('":')[1][1:-1]
        if 'selfUrl' in i:
            par['selfUrl']=i.split('":')[1][1:-1]
        if 'offlineurl' in i:
            par['offlineurl']=i.split('":')[1][1:-1]
    # 关闭连接
    conn.close()
    return par

#========================================
#log out:
def LogOut(username='201428002509008', pwd='M19910602'):
    par=GetInfo()
    for i in par.keys():
        print i,':',par[i]
    urlOut='http://210.77.16.21/eportal/logout.jsp?ms2g='+par['offlineurl']
    print urlOut
    # 定义一些文件头
    headers = {'Host': '210.77.16.21',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,zh-CN;q=0.7,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate'}
    # 与网站构建一个连接
    conn = httplib.HTTPConnection("210.77.16.21")
    # 开始进行数据提交   同时也可以使用get进行
    conn.request(method="POST", url=urlOut, headers=headers)
    # 返回处理后的数据
    response = conn.getresponse()
    res = response.read()
    print username + ':'
    print res
    # 关闭连接
    conn.close()

#========================================
#log in:
def LogIn(username='201428002509008', pwd='M19910602'):
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
    # 与网站构建一个连接
    conn = httplib.HTTPConnection("210.77.16.21")
    # 开始进行数据提交   同时也可以使用get进行
    conn.request(method="POST", url=loginurl, body=params, headers=headers)
    # 返回处理后的数据
    response = conn.getresponse()
    res = response.read()
    if 'success' in res.split(',')[1]:
        print 1
    conn.close()

#========================================
#LogIn()
#for i in range(40):
#   username='201428002826'+'%.3d'%i
#   pwd='ucas'
#   LogIn(username=username,pwd=pwd)
#   username='201328002826'+'%.3d'%i
#   pwd='ucas'
#   LogIn(username=username,pwd=pwd)
##LogIn('201428003922031', '299792458')
#LogIn('201428002826018', 'ucas')
#GetInfo()
LogOut('201428002826018', 'ucas')

