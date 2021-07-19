# Enter your code here. Read input from STDIN. Print output to STDOUT

'''at least 3 boys means family can have also 4,5 or 6 boys
A - baby is a girl
B - baby is a boy
P(B) = 1.09/ 2.09
P(A) = 1/ 2.09

families with exactly 6 children will have at least 3 boys means :
family = {3 boys, 4 boys, 5 boys, 6 boys}

'''

#this function generate and return factorial value of given number.
def factorial(n):
    fact =1
    for i in range(n):
        fact = fact * (i+1)
    return fact

if __name__ == "__main__":
    n = 6
    girl = 1
    boy = 1.09
    P_girl = girl/(girl + boy)
    P_boy = 1-P_girl
    val =0
    for i in range(3):
        r =  i
        val = val + ((factorial(n)/(factorial(n-r)* factorial(r))) * pow(P_boy,r)* pow(P_girl,n-r))
    
    ans = 1- val
    print(round(ans,3))
          
    
    
