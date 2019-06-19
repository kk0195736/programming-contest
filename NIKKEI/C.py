import numpy as np

N = int(input())

A = [0 for i in range(N)]
B = [0 for i in range(N)]
C = [0 for i in range(N)]

for i in range(N):
    A[i], B[i] = map(int, input().split())
    C[i] = A[i] + B[i]

C.sort(reverse=True)

ans = 0

for i in range(N):
    if i % 2 == 0:
        ans += C[i]

print(ans - sum(B))
