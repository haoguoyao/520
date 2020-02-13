#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:25:46 2020

@author: apple
"""

class states:
    #each state in a tuple
    def __init__(self,size_x,size_y):
        #2 means not observed, 1 means blocked, 0 means opened
        self.observed = [[2 for _ in range(size_x)] for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        self.initialize()
    def one_blocked(self,x,y):
        self.observed[x][y] = 1
    def one_opened(self,x,y):
        self.observed[x][y] = 0
    def initialize(self):
        self.search = [[0 for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.g =[[0 for _ in range(self.size_x)] for _ in range(self.size_y)]
    def set_start(self,start):
        self.g[start[0]][start[1]] = 0
    def set_goal(self,goal):
        self.g[goal[0]][goal[1]] = int('inf')
    def succ(self,current):
        next_move = []
        if current[0]>=1:
            next_move.append((current[0]-1,current[1]))
        if current[1]>=1:
            next_move.append((current[0],current[1]-1))
        if current[0]<self.size_x:
            next_move.append((current[0]+1,current[1]))
        if current[1]<self.size_y:
            next_move.append((current[0],current[1]+1))
        return next_move
