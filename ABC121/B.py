N,M,C = list(map(int, input().split()))

B = list(map(int, input().split()))
A = []

ans = 0

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(N):
    k = C
    for j in range(M):
        k += A[i][j] * B[j]
    if k > 0:
        ans += 1
    
print(ans)