N, K = list(map(int, input().split()))
S = input()
s = []

co = 1
for i in range(N-1):
    if S[i] != S[i+1]:
        s.append(co)
        co = 1
    else:
        co += 1

s.append(co)

ans = []

for i in range(len(s)):
    if S[0] == '0':
        ans.append(sum(s[i:K*2+i]))
    else:
        ans.append(sum(s[i:K*2+1+i]))

print(max(ans))