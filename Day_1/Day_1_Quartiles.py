#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

#this function calculate median of given list
def findmedian(num):
    l=int((len(num)-1)/2)
    u=int(len(num)/2)
    return int((num[l]+num[u])/2)
    

    
def quartiles(arr):
    
    length = len(arr)
    
    #sort arr array
    arr.sort()
    ans =[]
    
    #no matter length even or odd second quartile can calculate same way becaus second quartile is the median of array
    second_qrt = findmedian(arr)
    
    #for length = even number arrays
    if length % 2 ==0:
        first_quartileArray_upperLimit = int(length/2)
        LowArr = arr[0:first_quartileArray_upperLimit]
        HighArr = arr[first_quartileArray_upperLimit:length]
        first_qrt = findmedian(LowArr)
        third_qrt = findmedian(HighArr)
    #for length = odd number array
    else:
        first_quartileArray_upperLimit = int(length/2)
        LowArr = arr[0:first_quartileArray_upperLimit]
        HighArr = arr[first_quartileArray_upperLimit+1:length]
        first_qrt = findmedian(LowArr)
        third_qrt = findmedian(HighArr)
    ans.append(first_qrt)
    ans.append(second_qrt)
    ans.append(third_qrt)
    return ans
    
        
    
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
