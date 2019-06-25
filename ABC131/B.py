N, L = list(map(int, input().split()))

S = []

for i in range(N):
    S.append(abs(L+i))

mi = min(S)

su = int(N * (L + (L+N-1)) / 2)

if su < 0:
    print(su+mi)
else:
    print(su-mi)