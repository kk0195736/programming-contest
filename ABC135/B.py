N = int(input())
p = list(map(int, input().split()))
pp = p[:]
p.sort()
count = 0

for i in range(len(p)):
    if p[i] != pp[i]:
        count += 1
    else:
        pass

if count == 2 or count== 0:
    print('YES')
else:
    print('NO')