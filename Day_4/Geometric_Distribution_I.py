numerator,denominator = input().split()
first_defect = int(input())

#probability of machine produces a defective product
p = int(numerator) / int(denominator)
q = 1- p
n = first_defect

#Applying to equation ( qn-1 . p)
ans = pow(q,n-1) * p

print(round(ans,3))
