Data Structure Course Project

Data Structure and Algorithm using python


Project 1: To implement a stack using linkedlist, performed a depth first search and also familiar with command line arguments

To run the program, simply "python DFS.py m1.txt 0.5 True/False". 

sys.arg 1 represents the maze we are going to run. 
sys.arg 2 represents the time delay for each step.
sys.arg 3 represents the Flag, meaning the detection sequence. When it is false, we will detect as top, right, bot and left. When it is true, the detection sequence will be random and we will run the maze for 30 times. Then get the mean, std of the 30 runs.

Project 2: Some improvement over the project 1 includes implementing the heuristic algorithm A* to find the optimal path, https://en.wikipedia.org/wiki/A*_search_algorithm wikipedia page.

To run the program, simply "python Astar.py m1.txt 0.5 1"

sys.arg 1 represents the maze we are going to run. 
sys.arg 2 represents the time delay for each step.
sys.arg 3 represents the value for epsilon, refer to the wikipedia doc for th function of epsilon. 


Sorting_Algorithm: 

1. Compared the different soring algorithms, bubble sort, merge sort, insertion sort and bucket sort. 
2. Also did some analysis on the efficiency of these algorithms. 
3. For merge sort, also tried to find out the best threshold that could be used given different array size. 

