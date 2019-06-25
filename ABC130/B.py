N, X = list(map(int, input().split()))

L = list(map(int, input().split()))


now = 0
i = 0
while True:
    if now > X:
        break
    now += L[i]
    i += 1

print(i)