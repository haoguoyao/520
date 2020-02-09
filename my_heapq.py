#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:47:51 2020

@author: apple
"""
class my_heapq:
    def __init__(self):
        self.lst = []
    def push(self,num):
        self.lst.append(num)
        index = len(self.lst)-1
        while (index-1)/2>=0:
            if self.lst[index]<self.lst[(index-1)/2]:
                self.swap_position(index,(index-1)/2)
                index = (index-1)/2
            else:
                return
            
    def swap_position(self,x,y):
        temp = self.lst[x]       
        self.lst[x] = self.lst[y]
        self.lst[y] = temp
    def pop(self):
        if(len(self.lst)>0):
            result = self.lst[0]
        self.swap_position(0,len(self.lst)-1)
        self.lst.pop()
        index = 0
        while True:
            if (index*2+1)==len(self.lst)-1:
                if self.lst[index]>self.lst[index*2+1]:
                    self.swap_position(index, index*2+1)
                    index = index*2+1
                else:
                    return result
            if (index*2+1)>len(self.lst)-1:
                return result
            if (index*2+1)<len(self.lst)-1:       
                smaller = (index*2+1) if self.lst[index*2+1]<self.lst[index*2+2]else(index*2+2)
                if self.lst[index]<=self.lst[smaller]:
                    return result
                else:
                    self.swap_position(index,smaller)
                    index = smaller
    def show(self):
        print(self.lst)
        
