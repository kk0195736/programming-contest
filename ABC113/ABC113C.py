N, M = map(int, input().split())

P = []
Y = []
X = []
Xa = []

for i in range(M):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)
    X.append(p * 1000000 + y)

for i in P:
    c = 1
    for j in range(M):
        if (X[j] / 1000000) == (i + 1):
            Xa.append(c)
            c += 1

print(N, M, P, Y, X, Xa)
