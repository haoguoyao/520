#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:58:29 2020

@author: apple
"""

import random
import states as sts
import my_heapq

def print_maze():
    for j in range (0,size):
        for i in range(0,size):
            if i==start[0] and j==start[1]:
                print("s"),
            if i==target.i and j==target.j:
                print("t"),
            elif maze[i][j]==0:
                print (" "),
            else:
                print ("□"),
        print("")

def show_route(path):
        points = []
        for temp in path:
            points.append((temp.i,temp.j))
        for j in range (0,size):
            for i in range(0,size):
                if i==start[0] and j==start[1]:
                    print("s"),
                elif i==target.i and j==target.j:
                    print("t"),
                elif (i,j) in points:
                    print("*"),
                elif maze[i][j]==0:
                    print (" "),
                else:
                    print ("□"),
            print("")

                
def A_star_back():
    #print("########")
    global number_expaned_cells
    while len(opn_list.lst)>0 and agent > opn_list.peek():
        number_expaned_cells+=1
        s = opn_list.pop()
        s.closed = True
        succ = states.succ_back(agent,s)
        #print("+++++++++++++++++++")
        #print(len(succ))
        for i in succ:
            if i.search < counter:
                i.g=float("inf")
                i.search=counter
            if i.g > s.g+1:
                i.g = s.g+1
                i.node = s
                if(i.closed==False):
                    opn_list.push(i)               
number_expaned_cells = 0  
for repeat in range(0,30):
    size = 60
    
    maze = [[0 if random.random()>0.3 else 1  for _ in range(size)] for _ in range(size)]
    
    states = sts.states(size)
    counter = 0
    
    # initiate the start point and target point
    while True:
        agent = states.states[random.randint(0,size-1)][random.randint(0,size-1)]
        if(maze[agent.i][agent.j])==0:
            break
    start = (agent.i,agent.j)
    while True:
        target = states.states[random.randint(0,size-1)][random.randint(0,size-1)]
        if(maze[target.i][target.j])==0:
            break
    #print the maze    
    
    #print_maze()
    whole_path = []
    target.h = states.heuristic(agent, target)
    agent.h = 0
    states.set_target(target)
    
    while agent.i!=target.i or agent.j!=target.j:
    #for temp in range(1,100):
        print "In this round, the agent start with"
        print (agent.i,agent.j)
        counter = counter+1
        target.g = 0
        agent.g= float('inf')
        agent.search = counter
        opn_list = my_heapq.my_heapq()
        states.clear()
        opn_list.push(target)
        
        A_star_back()
        
        if opn_list.is_empty()==True:
            print("cannot reach target") 
            print_maze()
            break
        else:
            path = []
            #path.append(agent)
            next_node = agent.node
            path.append(next_node)
            while next_node!=target:
                next_node = next_node.node
                path.append(next_node)
#            for temp in path:
#                print (temp.i,temp.j)
            for node in path:
                #print("in path")
                #one cell is detected to be blocked
                if node.i>=1:
                    states.maze[node.i-1][node.j] = maze[node.i-1][node.j]
                if node.j>=1:
                    states.maze[node.i][node.j-1] = maze[node.i][node.j-1]
                if node.i<size-1:
                    states.maze[node.i+1][node.j] = maze[node.i+1][node.j]
                if node.j<size-1:
                    states.maze[node.i][node.j+1] = maze[node.i][node.j+1]
    
                if maze[node.i][node.j]==1:
                    states.maze[node.i][node.j] = 1
                    break
                else:
                    whole_path.append(node)
                    agent = node
                if node.i==target.i and node.j== target.j:
                    show_route(whole_path)
                    print("Reach the target")
                    

print (number_expaned_cells)
        
    

