a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))

h = [a1, b1, a2, b2, a3, b3]

c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in h:
    if i == 1:
        c1 += 1
    elif i == 2:
        c2 += 1
    elif i == 3:
        c3 += 1
    else:
        c4 += 1

ans = [c1, c2, c3, c4]

flag = False

for i in ans:
    if i == 3:
        flag = True

if flag == True:
    print("NO")
else:
    print('YES')