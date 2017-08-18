#!/usr/bin/env python
# coding=utf-8
#from UCAS import UCAS
#from login import LogIn
from creatALLid import CreatAllId
from run import Run
from read_par import read
import sys
par=read('./parameter')
if par['CreatAllId']:
    CREAT=CreatAllId()
#   CREAT.run()
    CREAT.run_Valid_accounts()

func=Run(pwd=par['passwd'],num=par['NumberToRun'])
func.WriteValidAccounts=par['WriteValidAccounts']
func.run()

