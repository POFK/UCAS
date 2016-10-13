#!/usr/bin/env python
# coding=utf-8
from urllib import urlopen

def logout():
    """logout"""

    url = r'http://210.77.16.21/eportal/InterFace.do?method=logout&userIndex='
    urlopen(url)

if __name__=='__main__':
    logout()

