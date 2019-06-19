N, M = list(map(int, input().split()))

C = []

for i in range(N):
    a, b = list(map(int, input().split()))
    C.append([a, b])

C.sort()

k = 0
ans = 0

for i in range(N):
    if k + C[i][1] <= M:
        k += C[i][1]
        ans += C[i][0] * C[i][1]
    
    else:
        ans += (M - k) * C[i][0]
        break

print(ans)