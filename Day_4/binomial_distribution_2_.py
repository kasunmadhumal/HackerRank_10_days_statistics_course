# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    fact =1
    for i in range(n):
        fact = fact * (i+1)
    return fact
if __name__ == "__main__":
    P_reject = 0.12
    fine = 1 - P_reject
    n = 10
    val =0
    for i in range(3):
        r = i
        val = val + ((factorial(n)/(factorial(n-r)* factorial(r))) * pow(P_reject,r)* pow(fine,n-r))
    
    
    val2 =0
    for i in range(2):
        r = i
        val2 = val2 + ((factorial(n)/(factorial(n-r)* factorial(r))) * pow(P_reject,r)* pow(fine,n-r))
    ans = 1-val2
    print(round(val,3))
    print(round(ans,3))
    
    
