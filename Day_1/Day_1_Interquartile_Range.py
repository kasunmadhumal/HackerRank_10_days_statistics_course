#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def findmedian(num):
    l=int((len(num)-1)/2)
    u=int(len(num)/2)
    return (num[l]+num[u])/2

    
    
    

def interQuartile(values, freqs):
    
    #number of different elements
    countValues = len(values)
    
    #count of all elements
    length = sum(freqs)
    

  
    create_array =[]
    
    ''' in create_array contains all elements with their frequences'''
    for i in range(countValues):
        for f in range(freqs[i]):
            create_array.append(values[i])
    
    '''after making create_array we can move to the Day_1 question 1 algorithm.
    because after making create_array both questions are same.'''
    create_array.sort()
    
        
    
    
    #for length = even number arrays
    if length % 2 ==0:
        first_quartileArray_upperLimit = int(length/2)
        LowArr = create_array[0:first_quartileArray_upperLimit]
        HighArr = create_array[first_quartileArray_upperLimit:length]
        first_qrt = findmedian(LowArr)
        third_qrt = findmedian(HighArr)


    #for length = odd number array
    else:
        first_quartileArray_upperLimit = int(length/2)
        LowArr =create_array[0:first_quartileArray_upperLimit]
        HighArr = create_array[first_quartileArray_upperLimit+1:length]
        first_qrt = findmedian(LowArr)
        third_qrt = findmedian(HighArr)
    
    # Print your answer to 1 decimal place within this function
    print(round (third_qrt-first_qrt,1)) 

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
