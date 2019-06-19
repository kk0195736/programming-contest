N = int(input())

a = []
b = []

for i in range(N-1):
    A, B = list(map(int, input().split()))
    a.append(A)
    b.append(B)

flag = False
for i in range(1, N+1):
    if not i in a:
        flag = True
        break
    if not i in b:
        flag = True
        break

if N % 2 == 0 and flag == False:
    print('Second')
elif N % 2 == 1 and flag == False:
    print('First')
elif N % 2 == 0 and flag == True:
    print('First')
else:
    print('Second')