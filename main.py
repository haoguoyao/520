#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:12:47 2020

@author: apple
"""
import random
import states as sts
import my_heapq
import sys
def A_star():
    while len(opn_list.lst)>0 and target > opn_list.peek():
        s = opn_list.pop()
        succ = states.succ(s)
        for i in succ:
#            if states.states[i[0]][i[1]] < counter:
#                states.states[i[0]][i[1]].g=int("inf")
#                states.states[i[0]][i[1]].search=counter
#            if states.states[i[0]][i[1]].g > states.states[s[0]][s[1]].g+1:
#                states.states[i[0]][i[1]].g = states.states[s[0]][s[1]].g+1
#                states.states[i[0]][i[1]].node = states.states[s[0]][s[1]]
#                opn_list.push(states.states[i[0]][i[1]])
            if i.search < counter:
                i.g=float("inf")
                i.search=counter
            if i.g > s.g+1:
                i.g = s.g+1
                i.node = s
                opn_list.push(i)
                
                

#main
size = 10
maze = [[0 if random.random()>0.3 else 1  for _ in range(size)] for _ in range(size)]
states = sts.states(maze)
counter = 0
while True:
    agent = states.states[random.randint(0,size-1)][random.randint(0,size-1)]
    if(maze[agent.i][agent.j])==0:
        break
while True:
    target = states.states[random.randint(0,size-1)][random.randint(0,size-1)]
    if(maze[target.i][target.j])==0:
        break
agent.h = states.heuristic(agent, target)
target.h = 0
states.set_goal(target)
states.show_maze()
#while agent!=target:
for temp in range(1,5):
    counter = counter+1
    agent.g = 0
    target.g= float('inf')
    agent.search = counter
    opn_list = my_heapq.my_heapq()
    opn_list.push(agent)
    print opn_list.lst
    A_star()
    if opn_list.is_empty()==True:
        print("cannot reach target")
        sys.exit()
    else:
        next_node = target.node
        while next_node.node!=agent:
            next_node = next_node.node
        agent = next_node
print("Reach the target")
        
    
