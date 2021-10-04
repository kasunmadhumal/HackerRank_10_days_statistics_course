'''
This code only makes the algorithm for the equation.
 If you want to get the theory behind this, please see the tutorial given.
'''

A,B = input().split(" ")
averageX, averageY = float(A), float(B)
CostX = 160 + 40*(averageX + pow(averageX,2))
CostY = 128 + 40*(averageY + pow(averageY,2))

print(round(CostX, 3))
print(round(CostY, 3))

