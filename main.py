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
def print_maze():
    for j in range (0,size):
        for i in range(0,size):
            if i==start_remember[0] and j==start_remember[1]:
                print("s"),
            if i==target.i and j==target.j:
                print("t"),
            elif maze[i][j]==0:
                print (" "),
            else:
                print ("□"),
        print("")
def A_star():
    while len(opn_list.lst)>0 and target > opn_list.peek():
        s = opn_list.pop()
        s.closed = True
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
                if(i.closed==False):
                    opn_list.push(i)
                
                


size = 30
maze = [[0 if random.random()>0.3 else 1  for _ in range(size)] for _ in range(size)]

states = sts.states(size)
counter = 0

# initiate the start point and target point
while True:
    agent = states.states[random.randint(0,size-1)][random.randint(0,size-1)]
    if(maze[agent.i][agent.j])==0:
        break
start_remember = (agent.i,agent.j)
while True:
    target = states.states[random.randint(0,size-1)][random.randint(0,size-1)]
    if(maze[target.i][target.j])==0:
        break
#print the maze    

print_maze()
whole_path = []
agent.h = states.heuristic(agent, target)
target.h = 0
states.set_target(target)

while agent!=target:
#for temp in range(1,100):
    print "In this round, the agent start with"
    print (agent.i,agent.j)
    counter = counter+1
    agent.g = 0
    target.g= float('inf')
    agent.search = counter
    opn_list = my_heapq.my_heapq()
    states.clear()
    opn_list.push(agent)
    print opn_list.lst
    A_star()
    if opn_list.is_empty()==True:
        print("cannot reach target")
        #print the maze    
        print_maze()
        sys.exit()
    else:
        path = []
        path.append(target)
        next_node = target.node
        path.append(next_node)
        while next_node.node!=agent:
            next_node = next_node.node
            path.append(next_node)
        path.reverse()
        for temp in path:
            print (temp.i,temp.j)
        for node in path:
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

def show_route(path):
    points = []
    for temp in path:
        print(temp.i,temp.j)
        points.append((temp.i,temp.j))
    for j in range (0,size):
        for i in range(0,size):
            if i==start_remember[0] and j==start_remember[1]:
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
show_route(whole_path)
print("Reach the target")
        
    
