N, A, B = list(map(int, input().split()))
if B != 0:
    D = list(map(int, input().split()))
else:
    print(0)
    exit()
ans = N - B

D.append(0)
D.append(N+1)
D.sort()

for i in range(1,len(D)):
    a = D[i] - D[i-1] -1
    if a >= A:
        ans -= int(a / A)

print(ans)