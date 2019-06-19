N, M = list(map(int, input().split()))

X = list(map(int, input().split()))

x = []
X.sort()

for i in range(1,M):
    x.append(abs(X[i] - X[i-1]))
x.sort(reverse=True)


ans = sum(x)

if N >= len(X):
    print(0)
else:
    for i in range(N - 1):
        ans -= x[i]

    print(ans)