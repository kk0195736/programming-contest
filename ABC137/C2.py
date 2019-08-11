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
    s.append(''.join(S))

s.sort()

ss = list(set(s))

co = [0]*len(ss)

for i in range(len(ss)):
    co[i] += s.count(ss[i])

ans = 0

for i in co:
    if i != 1:
        ans += cmb(i,2)

print(ans)