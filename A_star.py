# -*- coding: utf-8 -*-

import random
import states as sts
import my_heapq

class A_star_parent:
    def __init__(self,maze,position1,position2,size,heuristic = "manhattan",tie="bigger"):
        self.start = position1
        self.maze = maze
        self.size = size
        if(tie=="bigger"):
            self.states = sts.states(size)
        if(tie=="smaller"):
            self.states = sts.states(size,heuristic,tie)
        self.agent =  self.states.states[position1[0]][position1[1]]
        self.target =  self.states.states[position2[0]][position2[1]]
        if(self.maze[self.target.i][self.target.j])==1:
            while True:
                print("Target position wrong")
        #print self.agent
        #print self.target
        self.number_expaned_cells = 0
        self.opn_list = my_heapq.my_heapq()
        self.counter = 0

    def print_maze(self):
        for j in range (0,self.size):
            for i in range(0,self.size):
                if i==self.start[0] and j==self.start[1]:
                    print("s"),
                if i==self.target.i and j==self.target.j:
                    print("t"),
                elif self.maze[i][j]==0:
                    print (" "),
                else:
                    print ("□"),
            print("")

    def show_route(self,path):
            points = []
            for temp in path:
                print(temp.i,temp.j)
                points.append((temp.i,temp.j))
            for j in range (0,self.size):
                for i in range(0,self.size):
                    if i==self.start[0] and j==self.start[1]:
                        print("s"),
                    elif i==self.target.i and j==self.target.j:
                        print("t"),
                    elif (i,j) in points:
                        print("*"),
                    elif self.maze[i][j]==0:
                        print (" "),
                    else:
                        print ("□"),
                print("")
                
    
        
    
