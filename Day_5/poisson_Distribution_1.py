import math

'''
This code only makes the algorithm for the equation.
 If you want to get the theory behind this, please see the tutorial given.
'''
lmd = float(input())
k = int(input())
ans = (pow(lmd,k) * pow(math.e , -lmd))/ math.factorial(k)
print(round(ans,3))