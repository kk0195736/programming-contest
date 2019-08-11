N, M = list(map(int, input().split()))

ab = []

for i in range(N):
    a, b = list(map(int, input().split()))
    ab.append([a,b])

ab.sort()
ans = 0

now = M - 1

for i in range(M):
    if ab