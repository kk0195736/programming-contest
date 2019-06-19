import random

def low(str):
    if '#' in str:
        return False
    else:
        return True

H, W = list(map(int, input().split()))
c = []

for i in range(H):
    c.append(input())

flag = False
f = []
for j in c:
    f.append(low(j))
    if low(j):
        flag = True

if flag == False:
    print(':(')

else:
    if W >= 50:
        print(':(')
    else:
        print('Yay!')