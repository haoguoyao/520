# -*- coding: utf-8 -*-

import A_star_back as ab
import A_star_forward as af
import A_star_adaptive as ad
import random
import time
import matplotlib.pyplot as plt
lst_forward = []
lst_forward_smaller = []
lst_back = []
lst_forward_time = []
lst_back_time = []
lst_forward_smaller_time = []
lst_adaptive = []
lst_adaptive_time = []

repeat_times = 50
for repeat in range(0,repeat_times):
    size = 101
    
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
    time1 = time.time()
    forward = af.A_star_forward_cls(maze,position1,position2,size)
    forward.begin()
    time2 = time.time()
    back = ab.A_star_back_cls(maze,position1,position2,size)
    back.begin()
    time3 = time.time()
    

    forward_smaller = af.A_star_forward_cls(maze,position1,position2,size,heuristic = "manhattan",tie="smaller")
    forward_smaller.begin()
    time4 = time.time()
    adaptive = ad.A_star_adaptive_cls(maze,position1,position2,size)
    adaptive.begin()
    time5 = time.time()


    lst_forward.append(forward.number_expaned_cells)
    lst_back.append(back.number_expaned_cells)
    lst_forward_smaller.append(forward_smaller.number_expaned_cells)
    lst_adaptive.append(adaptive.number_expaned_cells)
    lst_adaptive_time.append(time5-time4)
    lst_forward_time.append(time2-time1)
    lst_forward_smaller_time.append(time4-time3)
    lst_back_time.append(time3-time2)


plt.plot(range(0,repeat_times),lst_forward,label="forward")
plt.plot(range(0,repeat_times),lst_adaptive,label="adaptive")
plt.legend()
plt.ylabel('Number of nodes expanded')
plt.title('Compare of Forward and Aadptive nodes')
plt.show()


plt.plot(range(0,repeat_times),lst_forward_time,label="forward")
plt.plot(range(0,repeat_times),lst_adaptive_time,label="adaptive")
plt.legend()
plt.ylabel('Time')
plt.title('Compare of Forward and Aadptive time')
plt.show()





plt.plot(range(0,repeat_times),lst_forward,label="forward")
plt.plot(range(0,repeat_times),lst_back,label="backward")
plt.legend()
plt.ylabel('Number of nodes expanded')
plt.title('Compare of Forward and Backward')
plt.show()


plt.plot(range(0,repeat_times),lst_forward_time,label="forward")
plt.plot(range(0,repeat_times),lst_back_time,label="backward")
plt.legend()
plt.ylabel('time')
plt.title('Compare of Forward and Backward time')
plt.show()

plt.plot(range(0,repeat_times),lst_forward,label="tie with larger G-value")
plt.plot(range(0,repeat_times),lst_forward_smaller,label="tie with smaller G-value")
plt.legend()
plt.ylabel('time')
plt.title('The Effects of Ties')
plt.show()
