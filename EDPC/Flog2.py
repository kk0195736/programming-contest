N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

inf = float('inf')

DP = [inf] * N
DP[0] = 0

for i in range(N-1):
    for j in range(1, K+1):
        if i + j == N:
            break
        if DP[i+j] >= DP[i] + abs(h[i] - h[i+j]):
            DP[i+j] = DP[i] + abs(h[i] - h[i+j])
        else:
            pass

print(DP[-1])