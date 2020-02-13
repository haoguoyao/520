#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:33:30 2020

@author: apple
"""
import random


b = [[0 if random.random()>0.3 else 1  for _ in range(51)] for _ in range(51)]
for i in range (0,51):
    for j in range(0,51):
        if b[i][j]==0:
            print (" "),
        else:
            print ("□"),
    print("")
#print b