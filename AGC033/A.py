H, W = list(map(int, input().split()))
A = []
Black = 0
White = 0

for i in range(H):
    a = input()
    A.append(list(a))

for i in A:
    for j in i:
        if j == '.':
            White += 1
        else:
            Black += 1