def check(S):
    ans = 0
    for i in range(1,len(S)):
        if S[i-1] == 'A' and S[i] == 'B':
            ans += 1
    return ans

N = int(input())
s = []
a = 0
b = 0
ab = 0

ans = 0

for i in range(N):
    S = input()
    ans += check(S)
    if S[0] == 'B' or S[-1] == 'A':
        s.append(S)
        if S[0] == 'B' and S[-1] != 'A':
            b += 1
        elif S[0] != 'B' and S[-1] == 'A':
            a += 1
        else:
            ab += 1

if ab == 0:
    ans += min(a,b)
else:
    if a == 0 and b == 0:
        ans += ab - 1
    else:
        ans += ab + min(a,b)

print(ans)