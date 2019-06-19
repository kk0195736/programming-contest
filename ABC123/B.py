A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

S = [A,B,C,D,E]

s = []

for i in S:
    if i%10 != 0:
        s.append(i%10)

s.sort()

ans = 0

for i in S:
    if i%10 == 0:
        ans += i
    else:
        ans += i + 10 - i%10
if len(s) != 0:
    print(ans - 10 + s[0])
else:
    print(ans)