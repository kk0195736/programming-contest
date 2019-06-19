N, K = list(map(int, input().split()))
S = input()
s = []
a = S[K-1].lower()

for i in range(N):
    if i == K-1:
        s.append(a)
    else:
        s.append(S[i])

print(''.join(s))