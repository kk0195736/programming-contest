'''
import math

def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def gcd_list(arr):

    ans = arr[0]
    for c in arr[1::]:
        ans = gcd(ans , c)
    return ans
'''
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

N = int(input())

A = list(map(int, input().split()))
A.sort()

af = A[0]
ag = A[1]

F = make_divisors(af)
G = make_divisors(ag)
F.sort(reverse=True)
G.sort(reverse=True)
del F[-1]
del G[-1]

'''
print(F)
print(G)
'''

ansf = 1
ansg = 1

for i in F:
    count = 0
    for j in A:
        if j % i != 0:
            count += 1
            if count == 2:
                break

    if count == 1:
        ansf = i
        break
    if count == 0:
        ansf = i
        break

for i in G:
    count = 0
    for j in A:
        if j % i != 0:
            count += 1
            if count == 2:
                break

    if count == 1:
        ansg = i
        break

print(max(ansf,ansg))
'''
g = gcd_list(A)
print(g)

for i in range(N):
    tmp = A.pop(0)
    if g < gcd_list(A):
        g = gcd_list(A)
    A.append(tmp)

print(g)
'''