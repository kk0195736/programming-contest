N = int(input())

u = []
v = []
w = []

for i in range(N-1):
    U, V, W = list(map(int, input().split()))
    u.append(U)
    v.append(V)
    w.append(W)

print(u,v,w)