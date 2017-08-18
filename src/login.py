#!/usr/bin/env python
# coding=utf-8
from UCAS import UCAS
import httplib
import urllib
class LogIn(UCAS):
    # ================================================================================
    def __init__(self):
        self.loginurl = 'http://210.77.16.21/eportal/InterFace.do?method=login'
    # 与网站构建一个连接
    #conn = httplib.HTTPConnection("210.77.16.21")
    # log in:
    def run(self,username='201428002509008', pwd='M19910602'):
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
        conn.request(method="POST", url=self.loginurl, body=params, headers=headers)
        # 返回处理后的数据
        response = conn.getresponse()
        res = response.read()
#       print username,pwd,res[1:-1].split(',"')[2].split(':')[1]
        conn.close()
        if 'success' in res.split(',')[1]:
            print username + ':'
            print res
            return 'success'
        elif res[1:-1].split(',"')[2].split(':')[1].find('用户不存在') != -1 :
            return 'errorID'      # username is a wrong ID, and can't log in.
        elif res[1:-1].split(',"')[2].split(':')[1].find('密码不匹配') != -1 :
            return 'errorPW'
        else:
            print 'error!', username, res
            return 0

if __name__ == '__main__':
    username = '201428012215040'
    pwd = 'ucas'
    f=LogIn()
    print f.run(username=username, pwd=pwd)
