N = int(input())
h = list(map(int, input().split()))

INF = float('inf')

DP = [INF] * N

DP[0] = 0
DP[1] = abs(h[1] - h[0])

for i in range(2,N):
    one = abs(h[i] - h[i-1]) + DP[i-1]
    two = abs(h[i] - h[i-2]) + DP[i-2]
    DP[i] = min(one,two)

print(DP[N-1])