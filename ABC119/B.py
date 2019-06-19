N = int(input())

x = []

for i in range(N):
    X, U = list(map(str, input().split()))
    if U == 'BTC':
        X = float(X) * 380000.0
    x.append(float(X))

print(sum(x))
