N, K = list(map(int, input().split()))

a = list(map(int, input().split()))

now = 0
ans = 0

while True:
    if now == N-1:
        if a[now] >= K:
            ans += 1
        break
    su = 0
    for i in range(now,N):
        su += a[i]
        if su >= K:
            ans += N-i
            break
    now += 1

print(ans)