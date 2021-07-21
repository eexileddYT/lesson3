#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:53:46 2021

@author:蔡侑廷
"""

x= input('number?')
x= int(x)
import random
a= random.randint(1,10)

if x == a:
    print('correct')
else:
    print('no')