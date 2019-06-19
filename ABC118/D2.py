N, M = list(map(int, input().split()))

A = []
A2 = A

for i in range(M):
    a = list(map(int, input().split()))
    A.append(a)

A2.sort()
B = []

for i in range(1,N):
    for j in range(1,N+1):
        if i < j:
            B.append([i,j])
print(A2)
print(B)

print(A2.pop())