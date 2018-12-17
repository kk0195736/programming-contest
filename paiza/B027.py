H, W, N = list(map(int, input().split()))

t = []

for i in range(H):
    T = list(map(int, input().split()))
    t.append(T)

L = int(input())

a = []
b = []
A = []
B = []

for i in range(L):
    v, w, x, y = list(map(int, input().split()))
    a.append(v-1)
    b.append(w-1)
    A.append(x-1)
    B.append(y-1)

got = [0 for i in range(N)]

player = 1

for i in range(L):
    if t[a[i]][b[i]] == t[A[i]][B[i]]:
        got[player - 1] += 2
    else:
        player += 1
        if player == N+1:
            player = 1

for i in range(N):
    print(got[i])