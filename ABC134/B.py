N, D = list(map(int, input().split()))

d = D*2 + 1

if N % d == 0:
    print(int(N//d))
else:
    print(int(N//d)+1)