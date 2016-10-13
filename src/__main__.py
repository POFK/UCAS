#!/usr/bin/env python
# coding=utf-8
#from UCAS import UCAS
#from login import LogIn
from creatALLid import CreatAllId
from run import Run
from read_par import read
import sys
par=read(sys.path[0]+'parameter')
if par['CreatAllId']:
    CreatAllId.run()

f=Run(pwd=par['passwd'],num=par['NumberToRun'])
f.run()

