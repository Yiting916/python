def fact(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def P(n, m):
    return fact(n)//fact(n-m)

def C(n,m):
    return P(n,m)//fact(m)

n1= eval(input())
n2= eval(input())
print(C(n1,n2))
