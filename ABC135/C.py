N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = sum(A)

yojo = 0
ne = B[0]

for i in range(N):
    yojo = A[i] - ne
    if yojo == 0:
        if i != N-1:
            ne = B[i+1]

    elif yojo < 0:
        if i != N-1:
            ne = B[i+1] + abs(yojo)
    else:
        ans -= yojo
        if i != N-1:
            ne = B[i+1]

ne = ne - A[-2]
if A[-1] - ne > 0:
    ans -= abs(A[-1]-ne)

print(ans)