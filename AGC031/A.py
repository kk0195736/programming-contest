import math

N = int(input())
S = list(input())

a = 10 ** 9 + 7

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def total(n):
    result = 0
    for i in range(0,n):
        result += combinations_count(n,i)
    return result

