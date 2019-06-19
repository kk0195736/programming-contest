N, M = list(map(int, input().split()))

A = []


for i in range(N):
    A.append(list(map(str, input().split())))
    del A[i][0]

if N != 1:
    ans = set(A[0]) & set(A[1])

if N >= 3:
    for i in range(2,N):
        ans = ans & set(A[i])

if N >= 2:
    print(len(ans))
else:
    print(len(A[0]))