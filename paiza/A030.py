N = int(input())

a2 = list(map(int, input().split()))
a = [-1]
for i in a2:
    a.append(i-1)

b = [0 for i in range(N)]

c = []

for i in range(len(a)):
    counter = 0
    now = i
    while True:
        if a[now] == -1:
            c.append(counter)
            break
        else:
            now = a[now]
            counter += 1

for i in reversed(range(1,max(c)+1)):
    for j in range(N):
        if c[j] == i:
            b[a[j]] += 1 + b[j]

#print(a, b, c)

for i in b:
    print(i)

'''
def dp(i):
    if i == 0:
        return N-1
    else:
        counter = 0
        S = []
        for j in range(N-1):
            if a[j] == a[i-1]:
                counter += 1
                if j != i:
                    S.append(j+1)

        e = 0
        for j in range(len(S)):
            e += dp(S[j])

        return dp(a[i-1]) - counter - e

N = int(input())

a = list(map(int, input().split()))

b = [0 for i in range(N)]
'''
'''
for i in a:
    b[i-1] += 1

for i in range(1, N):
    if b[i] != 0:
        b[a[i-1]-1] += b[i]
'''
'''

for i in range(N):
    b[i] = dp(i)

for i in b:
    print(i)

'''