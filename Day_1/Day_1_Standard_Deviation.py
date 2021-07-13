#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    #count how many numbers in arr
    numOfElements = len(arr)
    
    #calculate mean
    mean = sum(arr)/numOfElements
    sumVal =0
    for i in arr:
        sumVal += pow((i-mean),2)
    
    #final answer
    answer = math.sqrt(sumVal/numOfElements)
    print(answer)
        
        
        
        
        
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
