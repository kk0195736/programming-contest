N = int(input())
A = []
B = []
C = []
now = 0

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append([a, b])

C.sort(key=lambda x:x[0])
C.sort(key=lambda x:x[1])

Flag = False

for i in range(N):
    now += C[i][0]
    if now > C[i][1]:
        Flag = True
        break

if Flag == True:
    print('No')
else:
    print('Yes')