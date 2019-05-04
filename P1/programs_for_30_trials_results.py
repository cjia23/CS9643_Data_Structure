from Maze import Maze
from App import App
import pygame
from pygame.locals import *
import numpy as np
import time
import csv
import sys
from Stack import Node,Stack
import random 

# You might want to make this

class DFS:
    def __init__(self,DFS):
        self.DFS = DFS
        
    def isLocValid(self,y, x):
        """check if the input position is valid.
        valid means that the x,y is smaller or equal to max or bigger or equal to 1"""
        if y < height and y>=0 and x < width and x >= 0:
            return True
        else:
            return False

    # You might want to make this	
    def getNextNeighbour(self,y, x, flag):
        """check top,right,bot,left in sequence"""
        check_top = self.isLocValid(y-1,x) and (m[y-1,x] in ( ' ','E'))
        check_right = self.isLocValid(y,x+1) and (m[y,x+1] in (' ', 'E'))
        check_bot = self.isLocValid(y+1,x) and (m[y+1,x] in( ' ', 'E'))
        check_left = self.isLocValid(y,x-1) and (m[y,x-1] in( ' ', 'E'))
        
        if flag == True:
            check_sequence = random.sample([(check_top,(y-1,x)), (check_right,(y,x+1)), 
                                            (check_bot,(y+1,x)), (check_left,(y,x-1))],4)
        else:
            check_sequence = check_sequence = [(check_top,(y-1,x)), (check_right,(y,x+1)), 
                                            (check_bot,(y+1,x)), (check_left,(y,x-1))]
        #print(check_sequence)
        if check_sequence[0][0]: 
                return check_sequence[0][1]
        elif check_sequence[1][0]: 
            return check_sequence[1][1]
        elif check_sequence[2][0]: 
            return check_sequence[2][1]
        elif check_sequence[3][0]: 
            return check_sequence[3][1]
        else:
            return None
        
    # You might want to make this
    def loadMaze(self,filename):
        arr = np.genfromtxt(filename,dtype = str, delimiter = 1,comments = None)
        return arr


def compareResults_30times():
    ###########Initialization################## 
    totalSteps = 0
    stepsInPath = 0
    
    filename = sys.argv[1]
    delay = float(sys.argv[2])
    
    try:
        if sys.argv[3].lower() == 'true':
            flag = True
        elif sys.argv[3].lower() == 'false':
            flag = False
        else:
            flag = False
    except IndexError:
        flag = False
    
    #initialize the DFS object
    DFS = DFS('DFS')
    m = DFS.loadMaze(filename)
    print(m)
    height, width = m.shape
    a = App(m)
    # Find the Start somehow
    for i in range(0,height):
        for j in range(0,width):
            if m[i,j] == 'S':
                y = i 
                x = j
                totalSteps = 1
    print("found the starting point and their axis is: " + " x: " + str(x) + " y: " + str(y))        
    # make the position a tuple -- remember, it's like a list, but with round brackets. 
    """s_pos: starting position
       cur_pos: current position
       nei_pos: neightbour position
       prev_pos: previous position
    """
    s_pos = (y,x)
    
    
    # make stack
    myStack = Stack()
    myStack.push(s_pos)
    
    
    # While stack is not empty...
    
    cur_pos = myStack.peek()
    
    nei_pos = DFS.getNextNeighbour(cur_pos[0],cur_pos[1],flag)
    
    
    while myStack.length() is not None:
        cur_pos = myStack.peek()
        nei_pos = nei_pos = DFS.getNextNeighbour(cur_pos[0],cur_pos[1],flag)
        a.on_init()
        a.on_render()
        time.sleep(delay)
        
        if m[cur_pos] in ('E','f'):
            print("we have found the exit.")
            m[cur_pos] = "f"
            break
        else:
            if nei_pos is not None and m[nei_pos] not in ('E','#','x'):
                #next neighbour available then proceed
                myStack.push(nei_pos)
                m[cur_pos] = 'p'
                m[nei_pos] = 'c'
                
            elif nei_pos is not None and m[nei_pos] == 'E':
                #next neighbour is the exit....
                myStack.push(nei_pos)
                m[cur_pos] = 'p'
                m[nei_pos] = 'f'
            elif nei_pos is None:
                #backtrack
                prev_pos = cur_pos
                m[prev_pos] = 'x'
                myStack.pop()
                
                
        totalSteps += 1
        #this session is for debugging
        #using to print out each step and result in the console
        print (str(totalSteps))
        #print('current position: '+' y: ' + str(cur_pos[0]) + ' x: ' + str(cur_pos[1]))
        #if nei_pos is not None:
        #    print('neighbour position: '+' y: ' + str(nei_pos[0]) + ' x: ' + str(nei_pos[1]))
        print(m)
        
    a.on_render()    
    stepsInPath = myStack.length()        
    
    print('Total Steps:\t' + str(totalSteps))
    print('Steps In Path:\t' + str(stepsInPath))

######list to record results:




