#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    
    #find length of list
    numOf_X_Val = len(X)
    
    #define variable to store sum of X*Y values.
    fx =0
    for i in range(numOf_X_Val):
        fx += X[i] * W[i]
    ans = fx/ sum(W)
    
    #they expected answer have only one floating point. Thats why answer round one floating point
    print(round(ans,1))
        
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
