#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:47:54 2020

@author: apple
"""

class state:
    def __init__(self,i,j):
        self.node = None
        self.closed = False
        self.g = None
        self.i = i
        self.j = j
        self.h = None
        self.search = 0
#    def __lt__(self,data):
#        if self.g+self.h < data.g+data.h:
#            return True
#        else:
#            return False
#    def __gt__(self,data):
#        if self.g+self.h > data.g+data.h:
#            return True
#        else:
#            return False
#    def __le__(self,data):
#        if self.g+self.h <= data.g+data.h:
#            return True
#        else:
#            return False
#    def __ge__(self,data):
#        if self.g+self.h >= data.g+data.h:
#            return True
#        else:
#            return False
    def __lt__(self,data):
        if 9999*self.g+10000*self.h < 9999*data.g+10000*data.h:
            return True
        else:
            return False
    def __gt__(self,data):
        if 9999*self.g+10000*self.h > 9999*data.g+10000*data.h:
            return True
        else:
            return False
    def __le__(self,data):
        if 9999*self.g+10000*self.h <= 9999*data.g+10000*data.h:
            return True
        else:
            return False
    def __ge__(self,data):
        if 9999*self.g+10000*self.h >= 9999*data.g+10000*data.h:
            return True
        else:
            return False
#    def __lt__(self,data):
#        if 100001*self.g+10000*self.h < 100001*data.g+10000*data.h:
#            return True
#        else:
#            return False
#    def __gt__(self,data):
#        if 100001*self.g+10000*self.h > 100001*data.g+10000*data.h:
#            return True
#        else:
#            return False
#    def __le__(self,data):
#        if 100001*self.g+10000*self.h <= 100001*data.g+10000*data.h:
#            return True
#        else:
#            return False
#    def __ge__(self,data):
#        if 100001*self.g+10000*self.h >= 100001*data.g+10000*data.h:
#            return True
#        else:
#            return False 
    def clear(self):
        self.closed = False