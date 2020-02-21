#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:58:29 2020

@author: apple
"""

import random
import states as sts
import my_heapq
import A_star as ast
class A_star_back_cls(ast.A_star_parent):

    def A_star_back(self):
        #print("########")
        while len(self.opn_list.lst)>0 and self.agent > self.opn_list.peek():
            self.number_expaned_cells+=1
            s = self.opn_list.pop()
            s.closed = True
            succ = self.states.succ_back(self.agent,s)
            #print("+++++++++++++++++++")
            #print(len(succ))
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
        self.print_maze()
        whole_path = []
        self.target.h = self.states.heuristic(self.agent, self.target)
        self.agent.h = 0
        self.states.set_target(self.target)
        
        while self.agent.i!=self.target.i or self.agent.j!=self.target.j:
            if self.states.maze[self.target.i][self.target.j]==1:
                break
        #for temp in range(1,100):
            print "In this round, the agent start with"
            print (self.agent.i,self.agent.j)
            self.counter = self.counter+1
            self.target.g = 0
            self.agent.g= float('inf')
            self.agent.search = self.counter
            self.opn_list = my_heapq.my_heapq()
            self.states.clear()
            self.opn_list.push(self.target)
            
            self.A_star_back()
            
            if self.opn_list.is_empty()==True:
                print("cannot reach target") 
                self.print_maze()
                break
            else:
                path = []
                #path.append(self.agent)
                next_node = self.agent.node
                path.append(next_node)
                while next_node!=self.target:
                    next_node = next_node.node
                    path.append(next_node)
                for node in path:
                    #print("in path")
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

                    

