import numpy as np

N, K = map(int, input().split())

t = [0 for i in range(N)]
d = [0 for i in range(N)]

data = []

for i in range(N):
    t[i], d[i] = map(int, input().split())
    data.append([t[i], d[i]])


while True:
    if N == K:
        break

    m = min(d)

    for i, j in d:
        if j == m and t.count(t[i]) >= 2:
            del t[i]
            del d[i]
            N -= 1
            continue
        
