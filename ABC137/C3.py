N = int(input())
s = []
ss = []
ss_count = []
ans = 0


for i in range(N):
    S = list(input())
    S.sort()
    st = ''.join(S)
    s.append(st)
    if st in ss:
        pass
    else:
        

print(ans)