H, W = list(map(int, input().split()))

a11, a12 = list(map(int, input().split()))

a21, a22 = list(map(int, input().split()))

a = [[0 for i in range(W)] for i in range(H)]

a[0][0] = a11
a[0][1] = a12
a[1][0] = a21
a[1][1] = a22

for i in range(2, H):
    a[i][0] = a[i-1][0] + a[1][0] - a[0][0]

for i in range(2, H):
    a[i][1] = a[i-1][1] + a[1][1] - a[0][1]


for i in range(2, H):
    for j in range(W):
        a[j][i] = a[j][i-1] + a[i][1] - a[i][0]

for i in range(H):
    for j in range(W):
        print(a[i][j], end=" ")
    print()
