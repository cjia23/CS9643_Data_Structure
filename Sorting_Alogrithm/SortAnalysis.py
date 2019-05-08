import numpy as np
import time
import matplotlib.pyplot as plt

class SortAnalysis:
    
    def bubbleSort(self, array):
        """Bubble Sort
            if the neighbour elements of an array is bigger, then we reverse
            the position of the element."""
        if isinstance(array,np.ndarray):
            length = array.size
            for i in range(length):
                for j in range(1,length-i):
                    if array[j-1] > array[j]:
                        array[j],array[j-1] = array[j-1],array[j]
            return array
        else:
            raise ValueError("input must be a numpy array")
    
    def insertionSort(self, array):
        """Insertion Sort
        assume the first element as being soirted, then take the next element
        compare to the first and put it to the correct position, repeat the
        steps until the end of the array
        """
        length = len(array)
        for i in range(1,length):
            selected = array[i]
            index = i-1
            while index >=0:
                if array[index] > selected:
                    array[index+1] = array[index]
                    array[index] = selected
                index -=1
        return array
        
    def _merge(self, array, array1, array2):
        """merge array1  and array2 into array
        assume array1, array2 are sorted and will iterate through them 
        to put whichever smaller values into array
        """
        if (isinstance(array, np.ndarray) and isinstance(array1,np.ndarray)
            and isinstance(array2,np.ndarray)):
            
            i = 0
            j = 0
            k = 0
            while i < array1.size and j < array2.size:
                if array1[i] < array2[j]:
                    array[k] = array1[i]
                    i += 1
                else:
                    array[k] = array2[j]
                    j += 1
                k += 1
            
            while i < array1.size:
                array[k] = array1[i]
                i += 1
                k += 1
                
            while j < array2.size:
                array[k] = array2[j]
                j += 1  
                k += 1
            return array
        
        else:
            raise ValueError("input array must be numpy arrays")
        
    
    def mergeSort(self, array):
        """Merge Sort
        divide the array into two parts revursively and sort them
        last step is to merge them 
        print sign is used to diagnose
        n equals to the size of the array
    
        """
        if isinstance(array,np.ndarray):
            #print("Splitting ",array)
            n= array.size
            if n <= 1:
                #print("Merging ",array)
                return array
            else:
                size = n // 2
                left = self.mergeSort(array[:size].copy())
                right = self.mergeSort(array[size:].copy())
                array = self._merge(array, left, right)
                return array
        else:
            raise ValueError("input must be a numpy array")
    
    def mergeSort2(self, array):
        """Merge Sort 2
        similar method but with different threshold size instead of 1
        threshold has been set to 5.
        n equals to the size of the array
        """
        if isinstance(array,np.ndarray):
            #print("Splitting ",array)
            n = array.size
            threshold = 30
            if n <= threshold:
                #print("Merging ",array)
                return self.insertionSort(array)
            else:
                size = n // 2
                left = self.mergeSort(array[:size].copy())
                right = self.mergeSort(array[size:].copy())
                array = self._merge(array, left, right)
                return array
        else:
            raise ValueError("input must be a numpy array")
            
    def bucketSort(self, array):
        """bucket sort 
           create a list of n list
           put the element into sub-bucket, index = floor of (N*element)
           then insertion sort the sub-bucket
           then add each element back to the array according to the sequence
        """
        if isinstance(array, np.ndarray):
            n = array.size 
            B = [[] for _ in range(n)]
            
            for i in range(n):
                index = int(n*array[i])
                B[index].append(array[i])

            #sort each individual list
            for i in range(n):
                self.insertionSort(B[i])
                #print(i,B[i])
            
            #add the sub-bucket element to result 
            result = []
            k = 0
            for i in range(n):
                for j in range(len(B[i])):
                    array[k] = B[i][j]
                    k += 1
            return result
        else:
            raise ValueError("input must be a numpy array")
    
    def fibonacciArray(self, n):
        """fibonacci Array is composed by recursive 
        array[i] = array[i-1] + array[i-2].
        this one starts 5, 8,....
        """
        if n < 2:
            raise ValueError("input n has to be bigger or equal to 2")
        else:
            array = np.zeros(n,dtype = int)
            array[0] = 5
            array[1] = 8
            for i in range(2,n):
                array[i] = array[i-1] + array[i-2]
            return array
            
    def runSort(self, sortName ,sizes, seed):
        """run Sort analysis
           input: sortName: for the sort function previously implemented;
                  sizes array for sequences of runs for the functions called
                  seed to make sure each run using the same sequence of random numbers
           output: record the elapsed times in the time array for each run;
                   then return the array
        """
        if (isinstance(seed, int) and isinstance(sizes, np.ndarray)):
            np.random.seed(seed)
            times = np.ndarray(sizes.size)
            
            for i in range(sizes.size):
                A = np.random.uniform(size = sizes[i])
                start = time.time_ns()
                sortName(A)
                elapsed = (time.time_ns() - start)/1000
                times[i] = elapsed
            return times
        else:
            raise ValueError("Input format not correct.")
    
    def runAnalysis(self, sortList, n, filename):
        """run analysis
           input: sort list for the list of sorting algorithms previously implemented
                  n for the number of runs to perform, fibonacci numbers from 5
                  filename for the filename to be saved
        """
        if (isinstance(sortList, list) and isinstance(n, int)):
            sizes = self.fibonacciArray(n)
            #np.random.seed(n)
            plt.clf()
            for sort_algorithm in sortList:
                times = self.runSort(sort_algorithm,sizes,n)
                plt.loglog(sizes, times)
                #print(times)
            
            sortNameList = []
            for i in range(len(sortList)):
                sortNameList.append(sortList[i].__name__)
            plt.legend(sortNameList)
            plt.xlabel("array size")
            plt.ylabel("runtime (microseconds)")
            plt.savefig(filename + ".pdf")
        else:
            raise ValueError("Input is not in the correct format")
        

#For testing purposes
#a = SortAnalysis()

#Run Time Analysis 1
#a.runAnalysis([a.bubbleSort,a.insertionSort,a.mergeSort,a.bucketSort],15,'comparison1')

#Run Time Analysis 2
#a.runAnalysis([a.mergeSort,a.bucketSort],30,'comparison2')

#Run Time Analysis 3
#From observation of Figure 1, at roughly size 30 insertion sort lost its advantage to mergeSort
#Best performing algorithm is bucketSort overall for large scale data 
#a.runAnalysis([a.mergeSort,a.mergeSort2,a.bucketSort],25,'comparison3')
#At size 1000, merge sort 2 would have the same performace as mergeSort
#the 30 threhold imporoves mergeSort on smaller arrays sizes, for larger ones
#it would have no improvement.


# Question 1 Response: 
#We recursively divide the arrays into smaller arrays until they get to 
#the size 1, for example for array 100, would be diveded into 2 size 50 arrays
#then to two size 25 arrays, so on and so forth. Then the algorithm will merge
#them in order from the smallest array.
#This strategy can be viewed as firstly to divide a big problems into smaller
#problems, then using the insertion sort(very quick at small sets sorting) to 
#conquer the sets

# Question 2 Response:
#Because the index of the bucket the element goes into is derived from value of 
#the element multiplying the array size. This ensures that the biggest value of
#the ith bucket is smaller than the smallest value in the (i+1)th bucket


# Question 3 Response:
#From the graph, we can roughly estimate bucket sort has O(n) time complexity
#merge sort has O(nlogn), insertion and bubble sort has O(n^2)


# Question 4 Response:
#For the graph, bucket sort outperforms merge sort in every way from small
#to large size arrays. This is maybe due to that our mergesort threshold has 
#been set to 1 and bucket sort is doing its best when the array is uniformly
#distributed along a range. Our input array has been initialized to be in the 
#of 0 to 1.


# Question 5 Response:
#merge sort 2 has a new threhold set to 30. So for array size smaller than 30,
#the insertion sort will be applied. This improves the merge sort for the smaller
#array. Overall it didn't beat bucket sort. However, our input array is uniformly
#distributed along the range 0 to 1. But in a real case, that will not always be 
#true. So the improved merge sort will have a better performance.
#
