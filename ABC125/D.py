N = int(input())
A = list(map(int, input().split()))

ans = 0

a = []
for i in A:
    ans += abs(i)
    a.append(abs(i))

gusu = False

count = 0
for i in A:
    if i == 0:
        gusu = True
        break
    if 0 > i:
        count += 1

if count % 2 == 0:
    gusu = True

if gusu == True:
    print(ans)
else:
    print(ans - min(a)*2)