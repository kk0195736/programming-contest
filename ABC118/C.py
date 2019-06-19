N = int(input())
A = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return a
    else:
        return gcd(y, a%y)

def gcd3(x, y, z):
    return gcd(gcd(x, y), z)

def gcd_array(arr):
    for i in range(2, len(arr)):
        

while True:
    flag = False
    B = []
    for i in A:
        if i % min(A) != 0:
            flag = True
            B.append(i % min(A))
    if flag == False:
        break
    A = B

    
print(A[0])