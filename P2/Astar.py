from Maze import Maze
from App import App
from PriorityQueue import PriorityQueue
import pygame
from pygame.locals import *
import numpy as np
import time
import csv
import sys

def oneRun(eps, filename):
    class Astar:
        def isLocValid(self,y, x):
            """check if the input position is valid. valid means 
            that the x,y is smaller or equal to max or bigger or equal to 1"""
            if y < height and y>=0 and x < width and x >= 0:
                return True
            else:
                return False
        
        def getNextNeighbour(self,y, x):
            """at each location, check the four directions,
            the sequence is to check top, right, bot, left,
            Return a list of valid positions.
            """
            check_top = self.isLocValid(y-1,x) and (m[y-1,x] in ( ' ','E'))
            check_right = self.isLocValid(y,x+1) and (m[y,x+1] in (' ', 'E'))
            check_bot = self.isLocValid(y+1,x) and (m[y+1,x] in( ' ', 'E'))
            check_left = self.isLocValid(y,x-1) and (m[y,x-1] in( ' ', 'E'))
            
            check_sequence = [(check_top,(y-1,x)), (check_right,(y,x+1)), 
                                                   (check_bot,(y+1,x)), (check_left,(y,x-1))]
            
            result = []
            if check_sequence[0][0]: 
                result.append(check_sequence[0][1])
            if check_sequence[1][0]: 
                result.append(check_sequence[1][1])
            if check_sequence[2][0]: 
                result.append(check_sequence[2][1])
            if check_sequence[3][0]: 
                result.append(check_sequence[3][1])
            return result
        
        
        def loadMaze(self,fName):
            #load the maze
            arr = np.genfromtxt(fName,dtype = str, delimiter = 1,comments = None)
            return arr
        
        
        # just the straight line distance to the end. 
        def heuristic(self, start, end):
        	return ((float(start[0]) - float(end[0]))**2 + 
                     (float(start[1]) - float(end[1]))**2)**(0.5)
        
        def calculatePriority(self,NumSteps, epsilon, start, end):
            """I implemented the static weighing, epsilon will be defaulted as 
               0. And we could pass a value to epsilon.
            """
            priority = NumSteps + self.heuristic(start, end) * (1+ epsilon)
            return priority
    ##program running#################################
    
    #initialize an object
    A = Astar()
    
    #load the maze
    m = A.loadMaze(filename)
    
    #height, width is the shape of the loaded maze
    height, width = m.shape
    
    #will turn off the App aplication if running for test, otherwise turn it on
    try:
        if sys.argv[3] == 'test':
            pass
        else:
            a = App(m)
    except IndexError:
        a = App(m)
        
    # Find the Start and End positions
    for y in range(len(m)):
    	for x in range(len(m[y])):
    		if m[y][x] == 'S':		
    			startPos = (y,x)
    		if m[y][x] == 'E':
    			endPos = (y,x)
    #print(startPos)
    #print(endPos)
    
    
    Q = PriorityQueue()
    totalSteps = 0
    stepsInPath = 0
    
    #generate the current position tuple and enqueue it to the priority queue
    curPos = (startPos, stepsInPath, A.calculatePriority(stepsInPath, 
                                                         eps,startPos, endPos))
    Q.enqueue(curPos[0], curPos[1], curPos[2])
    
    #first step action
    m[curPos[0]] = 'c'
    totalSteps += 1
    stepsInPath += 1
    
    #delay of time
    delay = float(sys.argv[2])
    
    
    # While queue is not empty, actual algorithm 
    while (len(Q) > 0):
    	# Algo goes here.
        #this session is for debugging. ignore it.
        #print (str(totalSteps))
        #print('current position: '+' y: ' + str(curPos[0][0]) + ' x: ' + str(curPos[0][1]))
        #print("No of items in Q: ", len(Q))
        #print(Q.pos_tuple)
        #print(m)
        #print()
        
        """1. mark the first step as x, then dequeue for the new curPos,
              new stepsInpath will also be the stepsInPath parameter 
           2. check if the current position is Exit,
              2.1 if yes, print the stepsInPath, change to 'f' and break the 
                  loop
              2.2 if no, change to 'c' and get all available neigbour positions,
                  add one more steps in path then enqueue all new neiPos to 
                  priority queue
                     2.2.1 if nPos is the Exit, then do nothing. next step ,
                     the current step will for sure be selected 
                     2.2.2 if nPos is not the Exit, we will mark it as 'p'
           3. then each time, we add totalSteps by 1
           4. if application is initialized, the we render it for each loop
        """
        m[curPos[0]] = 'x'
        curPos = Q.dequeue()
        stepsInPath = curPos[1]
        
        if m[curPos[0]] == 'E':
            stepsInPath += 1
            print("total number of steps to the end is: ", stepsInPath)
            m[curPos[0]] = 'f'
            break
        else:
            m[curPos[0]] = 'c'
            neiPos = A.getNextNeighbour(curPos[0][0],curPos[0][1])
            stepsInPath += 1
            
            for nPos in neiPos:
                Q.enqueue(nPos, stepsInPath, 
                          A.calculatePriority(stepsInPath, eps, nPos, endPos))
                if m[nPos] == 'E':
                    pass
                else:
                    m[nPos] = 'p'
        totalSteps += 1
        
        
        try:
            if sys.argv[3] == 'test':
                pass
            else:
                a.on_init()
                a.on_render()
                time.sleep(delay)
        except IndexError:
            a.on_init()
            a.on_render()
            time.sleep(delay)
        
    try:
        if sys.argv[3] == 'test':
            pass
        else:
            a.on_render()
            time.sleep(delay)
    except IndexError:
        a.on_render()
        time.sleep(delay)

    #print out the final results
    print('epsilon is: ', eps)
    print('input file is: ', filename)
    print('Total Steps:' + str(totalSteps))
    curPos = (curPos, stepsInPath, A.calculatePriority(stepsInPath, 
                                                        eps,curPos[0], endPos))
    print('Steps In Path:' + str(curPos[1]))
    return totalSteps, curPos[1]


######record for the expriment####################
import matplotlib.pyplot as plt

"""
   input argument:  1 for filename, 
                    2 for time delay,
                    3 if equals to test, we will do the test for CS9643B
                      if there is a float number, one run will be initiated
                      with epsilon values
                      otherwise, epsilon will be defaulted as 0 for one run.
"""

#epsilon values will depend on input arguments, here I will do the 10000 runs
try:
    if sys.argv[3] == 'test':
        #test mode for expriment in CS9643B
        eps = np.logspace(-1,2,1000,10)
        np.insert(eps,0,0)
    elif sys.argv[3]:
        #if there are input arg for eps, then cast it as float
        eps = float(sys.argv[3])
except IndexError:
    #default eps as 0
    eps =  float(0)

if isinstance(eps, float):
    #initiate one Run
    oneRun(eps, str(sys.argv[1]))
else:
    # list of files m5 to m10
    filename = []
    for i in range(5,11):
        name = 'm' + str(i)
        filename.append(name)
    
    #lists for store results
    totalSteps = []
    pathSteps = []
    
    #loop through files m5 to m10 firstly, then loop for each epsilon value
    for name in filename:
        for epsilon in eps:
            t,p = oneRun(epsilon, str(name+'.txt'))
            
            totalSteps.append(t)
            pathSteps.append(p)
    
        plt.clf()
        fig, ax1 = plt.subplots()
        
        color = 'tab:blue'
        ax1.semilogx(eps, totalSteps, color=color)
        ax1.set_xlabel('epsilon')
        ax1.set_ylabel('algorithm steps', color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        
        ax2 = ax1.twinx()
        color = 'tab:orange'
        ax2.plot(eps, pathSteps, color=color)
        ax2.set_ylabel('path steps', color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        plt.title('Algorithm Efficiency versus Solution Size for Maze'+name)
        
        plt.savefig(name+ '.pdf')
        totalSteps.clear()
        pathSteps.clear()

"""
   Discussion for questions:
       1. Point out any notable or interesting features in each of your in your plots;
          1.1 for M5.pdf
              because the Exit and Start are on a diagonal corner of the map with
              walls pointing to the Start, the path in steps is always 22, 
              regardless of the epsilons of the input. However as epsilons 
              increase, the total steps drops
          1.2 for M6.pdf
              the Exit and Start are on a diagonal position with walls pointing
              to the Exit, the path in steps increases and the total steps 
              decrease as epsilon increases.
          1.3 for M7.pdf
              the Exit and Start are also on the diagonal corners with smaller 
              walls spreading across the map.  As the epsilons increase gradually,
              the total steps decrease but are turbulent and the steps in Path
              increases.
          1.4 for M8.pdf
              the Exit and Start are at the mid points of upper and lower bound
              with walls spreading. As epsilons increase, the steps in Path is 
              the same, but total sptes initially drop then jumps. The best path
              is always the straight line, but with walls blocking in the midway
              horizontally, it will greatly slow down our search speed.
              
          1.5 for M9.pdf
              the Exit and Start are at the mid points of upper and lower bound
              with walls spreading. As epsilons increase, the steps in Path is
              the same, but total steps drops gradually. The best path is always
              straight line and the walls are blocking more vertically and don't
              block that much compared to M8.
          1.6 for M10.pdf
              the Exit and Start are at the mid points of upper and lower bound
              with walls spreading. As epsilons increase, the steps in Path is
              the same, but total steps drops gradually. The best path is always
              straight line down to the botttom. The total steps depend on the 
              the hosrizontal walls.
          As epsilons increase, that makes the heuristic part more important
          than the steps in path. This will direct the program to move faster 
          to the 'right' direction to the Exit. But sometimes, there can be 
          traps with correct directions but no way out as in M6. 
          
        2. Discuss what you can say about the best choice of ε given your 
        experiments? Explain your reason for choosing an optimal value of ε.
        
          As epsilons increase, that makes the heuristic part more important
          than the steps in path. This will direct the program to move faster 
          to the 'right' direction to the Exit. But sometimes, there can be 
          traps with correct directions but no way out as in M6.   
          
          For most cases, the total steps would decrease while steps in path 
          increase as epsilon increases. The best epsilon can be the one that 
          two lines intercept with each other.
          
          In some cases where the steps in path remain the same due to the local
          shape, then best epsilon should be the one with least total steps.
          
          In general, the best epsilon have to be chosen carefully depending on
          the importance of time of search VS optimal path as well as "local 
          traps" in the map.
        
              
"""















