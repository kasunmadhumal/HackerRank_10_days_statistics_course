# Enter your code here. Read input from STDIN. Print output to STDOUT

numerator,denominator = input().split()
first_defect = int(input())

#probability of machine produces a defective product
p = int(numerator) / int(denominator)
q = 1- p
n = first_defect


'''  this question we applied to the same algorithm we applied in the previous question. but in this question, we have to consider different scenarios.  '''
ans =0
for i in range(n):
    N = i +1
    
    #probability of machine produces a defective product
    ans = ans + pow(q,N-1) * p
    

print(round(ans,3))
