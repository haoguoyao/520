#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:12:47 2020

@author: apple
"""
import random
import states as sts
import my_heapq
import A_star as ast
class A_star_forward_cls(ast.A_star_parent):

    def A_star(self):
        while len(self.opn_list.lst)>0 and self.target > self.opn_list.peek():
            self.number_expaned_cells+=1
            s = self.opn_list.pop()
            s.closed = True
            succ = self.states.succ(s)
            for i in succ:
                if i.search < self.counter:
                    i.g=float("inf")
                    i.search=self.counter
                if i.g > s.g+1:
                    i.g = s.g+1
                    i.node = s
                    if(i.closed==False):
                        self.opn_list.push(i)
                    
               
    def begin(self):
        whole_path = []
        self.agent.h = self.states.heuristic(self.agent, self.target)
        self.target.h = 0
        self.states.set_target(self.target)
        
        while self.agent!=self.target:
        #for temp in range(1,100):
            print "In this round, the agent start with"
            print (self.agent.i,self.agent.j)
            self.counter = self.counter+1
            self.agent.g = 0
            self.target.g= float('inf')
            self.agent.search = self.counter
            self.opn_list = my_heapq.my_heapq()
            self.states.clear()
            self.opn_list.push(self.agent)
            self.A_star()
            if self.opn_list.is_empty()==True:
                print("cannot reach target") 
                #print_maze()
                break
            else:
                path = []
                path.append(self.target)
                next_node = self.target.node
                path.append(next_node)
                #while next_node!=agent:
                while next_node.node!=self.agent:
                    next_node = next_node.node
                    path.append(next_node)
                path.reverse()
    #            for temp in path:
    #                print (temp.i,temp.j)
                for node in path:
                    #one cell is detected to be blocked
                    if node.i>=1:
                        self.states.maze[node.i-1][node.j] = self.maze[node.i-1][node.j]
                    if node.j>=1:
                        self.states.maze[node.i][node.j-1] = self.maze[node.i][node.j-1]
                    if node.i<self.size-1:
                        self.states.maze[node.i+1][node.j] = self.maze[node.i+1][node.j]
                    if node.j<self.size-1:
                        self.states.maze[node.i][node.j+1] = self.maze[node.i][node.j+1]
        
                    if self.maze[node.i][node.j]==1:
                        self.states.maze[node.i][node.j] = 1
                        break
                    else:
                        whole_path.append(node)
                        self.agent = node
                    if node.i==self.target.i and node.j== self.target.j:
                        self.show_route(whole_path)
                        print("Reach the target")  

        
    
