#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:25:46 2020

@author: apple
"""
import state
import state2
class states:
    #each state in a tuple
    def __init__(self,size,heuristic = "manhattan",tie="bigger"):
        #1 means blocked, 0 means opened
        #self.observed = [[2 for _ in range(size_x)] for _ in range(size_y)]
        self.maze = [[0 for _ in range(size)] for _ in range(size)]
        #print maze
        #self.maze = maze
        self.size_x = len(self.maze)
        self.size_y = len(self.maze[0])
        self.initialize(tie)
        if heuristic == "manhattan":
            self.heuristic = self.manhattan_heuristic
        if heuristic == "improving":
            self.heuristic = self.improving_heuristic
    def set_target(self,target):
        self.target = target
    def set_start(self,start):
        self.start = start 
#    def one_blocked(self,x,y):
#        self.observed[x][y] = 1
#    def one_opened(self,x,y):
#        self.observed[x][y] = 0
    def initialize(self,tie):
        self.search = [[0 for _ in range(self.size_x)] for _ in range(self.size_y)]
        if(tie=="bigger"):
            self.states =[[state.state(i,j) for j in range(self.size_x)] for i in range(self.size_y)]
        if(tie=="smaller"):
            self.states =[[state2.state(i,j) for j in range(self.size_x)] for i in range(self.size_y)]

    def succ(self,current):
        next_move = []
        if current.i>=1:
            if self.maze[current.i-1][current.j]!=1:
                self.states[current.i-1][current.j].h = self.heuristic(current,self.target)
                next_move.append(self.states[current.i-1][current.j])
        if current.j>=1:
            if self.maze[current.i][current.j-1]!=1:
                self.states[current.i][current.j-1].h = self.heuristic(current,self.target)
                next_move.append(self.states[current.i][current.j-1])
        if current.i<self.size_x-1:
            if self.maze[current.i+1][current.j]!=1:
                self.states[current.i+1][current.j].h = self.heuristic(current,self.target)
                next_move.append(self.states[current.i+1][current.j])
        if current.j<self.size_y-1:
            if self.maze[current.i][current.j+1]!=1:
                self.states[current.i][current.j+1].h = self.heuristic(current,self.target)
                next_move.append(self.states[current.i][current.j+1])
        return next_move
    
    
    def succ_back(self,agent,current):
        next_move = []
        if current.i>=1:
            if self.maze[current.i-1][current.j]!=1:
                self.states[current.i-1][current.j].h = self.heuristic(current,agent)
                next_move.append(self.states[current.i-1][current.j])
        if current.j>=1:
            if self.maze[current.i][current.j-1]!=1:
                self.states[current.i][current.j-1].h = self.heuristic(current,agent)
                next_move.append(self.states[current.i][current.j-1])
        if current.i<self.size_x-1:
            if self.maze[current.i+1][current.j]!=1:
                self.states[current.i+1][current.j].h = self.heuristic(current,agent)
                next_move.append(self.states[current.i+1][current.j])
        if current.j<self.size_y-1:
            if self.maze[current.i][current.j+1]!=1:
                self.states[current.i][current.j+1].h = self.heuristic(current,agent)
                next_move.append(self.states[current.i][current.j+1])
        return next_move
    def manhattan_heuristic(self,position1,position2):
        return abs(position1.i-position2.i)+abs(position1.j-position2.j)
    def improving_heuristic(self,position1,position2):
        pass
    def clear(self):
        for i in range(0,self.size_x):
            for j in range(0,self.size_y):
                self.states[i][j].clear()

