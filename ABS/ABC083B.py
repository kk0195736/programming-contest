N, A, B = map(int, input().split())

ans = 0

for i in range(1, N+1):
    j = sum(list(map(int, list(str(i)))))
    if j >= A and j <= B:
        ans += i

print(ans)