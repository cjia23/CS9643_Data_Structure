from SortAnalysis import SortAnalysis
import numpy as np
from copy import copy

# Setup Sort Method Check
n = 100
A = np.random.rand(n)
sortedA = copy(A)
sortedA.sort()
a = SortAnalysis()

# Check Bubble Sort
B = copy(A)
a.bubbleSort(B)
print('Testing bubbleSort:')
print(all(B == sortedA))
print()

# Check Insertion Sort
B = copy(A)
a.insertionSort(B)
print('Testing insertionSort:')
print(all(B == sortedA))
print()

# Check Merge Sort
B = copy(A)
a.mergeSort(B)
print('Testing mergeSort:')
print(all(B == sortedA))
print()

# Check Merge Sort 2
B = copy(A)
a.mergeSort2(B)
print('Testing mergeSort2:')
print(all(B == sortedA))
print()

# Check Bucket Sort
B = copy(A)
a.bucketSort(B)
print('Testing bucketSort:')
print(all(B == sortedA))
print()

# Check Merge
C1 = np.random.rand(n//2)
C2 = np.random.rand(n//2)
C1.sort()
C2.sort()
C = np.concatenate((C1,C2))
sortedC = copy(C)
sortedC.sort()
a._merge(C,C1,C2)
print('Testing _merge')
print(all(C == sortedC))
print()

# Check Fibonacci Array
D = np.array([5,8,13,21,34])
E = a.fibonacciArray(5)
print('Testing fibonacciArray')
print(all(D == E))
try:
    a.fibonacciArray(1)
except (ValueError):
    print(True)
except:
    print(False)
print()

# Check RunSort
F = np.array([1,10,100,1000])
print('Testing runSort')
bT = a.runSort(a.bubbleSort,F,0)
mT = a.runSort(a.mergeSort,F,0)
print(bT[-1] > mT[-1])
iT = a.runSort(a.insertionSort,F,0)
bT = a.runSort(a.bucketSort,F,0)
print(iT[-1] > bT[-1])

# Check Analysis
a.runAnalysis([a.bubbleSort,a.bucketSort],10,'test')

