N = int(input())

A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))

    A.append(a)
    B.append(b)

A.sort()
B.sort()

Entrance = 0
Exit = 0


Entrance = A[int((N)/2)]
Exit = B[int((N)/2)]

ans = 0

for i in range(N):
    ans += abs(Entrance - A[i]) + abs(A[i] - B[i]) + abs(Exit - B[i])

print(ans)