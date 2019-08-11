K, X = list(map(int, input().split()))

T = X - K + 1

ans = []

for i in range(K*2 - 1):
    ans.append(T)
    T += 1

print(' '.join(map(str, ans)))