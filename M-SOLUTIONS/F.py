N = int(input())

A = []
ans = 0

for i in range(N-1):
    a = input()
    ans += a.count('0')
    A.append(a)

print(ans)