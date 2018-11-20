def dp(i, j):

N, W = map(int, input().split())

v = []
w = []

for i in range(N):
    V, m = map(int, input().split())
    v.append(V)
    w.append(m)