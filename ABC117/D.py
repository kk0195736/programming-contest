N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

ans = 0

if K == 0:
    print(sum(A))
    exit()

ma = 2 ** (len(bin(K))-3)

e = K + 1
for i in range(2 ** (N-1)):
    a = 0
    e -= 1
    for j in A:
        a += e ^ j
    if ans < a:
        ans = a

print(ans)

'''
for i in range(2 ** (len(bin(K))-3),K+1):
    a = 0
    for j in A:
        a += i ^ j
    if ans < a:
        ans = a
print(ans)
'''
'''
for i in range(K+1):
    a = 0
    for j in A:
        b = i ^ j
        print('{} XOR {} = {}'.format(i,j,b))
        a += i ^ j
    print(a)
    if ans < a:
        ans = a
'''
'''
print(ans)
print(2 ** (len(bin(K))-3))
'''

