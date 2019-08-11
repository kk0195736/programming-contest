nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

N = int(input())
s = []


for i in range(N):
    S = list(input())
    S.sort()
    s.append(S)

s.sort()

ans = 0

mae = s[0]
count = 0

for i in range(1,N):
    if mae == s[i]:
        count += 1
    else:
        if count != 0:
            ans += cmb(count+1, 2)
        else:
            pass
        count = 0
    mae = s[i]

if count != 0:
    ans += cmb(count+1,2)

print(ans)
