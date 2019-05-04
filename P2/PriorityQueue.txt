class PriorityQueue:
    def __init__(self, pos_tuple = None):
        """initialize the queue with an empty list
        """
        self.pos_tuple = []
        
    def __len__(self):
        """return the length of the list"""

        return len(self.pos_tuple)
		

    def enqueue(self, pos, stepsToMe, p):
        """1. create the tuple 
           2. if the list is empty, then append directly
              if it is not, then append to the end, then sort the list in 
              reverse order so that the ones with least priority will always
              be at the end.
        """
        
        newTuple = (pos, stepsToMe, p)
        if len(self) == 0:
            self.pos_tuple.append(newTuple)
        else:
            self.pos_tuple.append(newTuple)
            
            #sort the list
            self.pos_tuple.sort(key = lambda newTuple: newTuple[2],reverse = True)
        
        #for debugging purpose
        #print(self.pos_tuple)    

    def dequeue(self):
        """remove the ones based with least priority, 
        always at the end of the list"""
        pos = self.pos_tuple[len(self) - 1]
        self.pos_tuple.pop(len(self) - 1)
        return pos
    

        
        