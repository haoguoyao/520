# -*- coding: utf-8 -*-

import A_star_back as ab
import A_star_forward as af
import random
lst_forward = []
lst_back = []

for repeat in range(0,10):
    size = 100
    
    maze = [[0 if random.random()>0.3 else 1  for _ in range(size)] for _ in range(size)]

    
    # initiate the start point and target point
    while True:
        position1 = (random.randint(0,size-1),random.randint(0,size-1))
        if(maze[position1[0]][position1[1]])==0:
            break
    while True:
        position2 = (random.randint(0,size-1),random.randint(0,size-1))
        if(maze[position2[0]][position2[1]])==0:
            #the target is different from the start position
            if position2[0]!=position1[0] or position2[1]!=position1[1]:
                break
    forward = af.A_star_forward_cls(maze,position1,position2,size)
    forward.begin()
    lst_forward.append(forward.number_expaned_cells)
    back = ab.A_star_back_cls(maze,position1,position2,size)
    back.begin()
    lst_back.append(back.number_expaned_cells)
print lst_forward
print lst_back