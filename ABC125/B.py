N = int(input())

V = list(map(int, input().split()))
C = list(map(int, input().split()))

a = []

for i in range(N):
    if V[i] - C[i] > 0:
        a.append(V[i] - C[i])

print(sum(a))