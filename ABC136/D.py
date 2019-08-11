S = input()

s = list(S)
s2 = []

ans = [0]*len(s)
countR = 1
countL = 1
mae = s[0]

for i in range(1,len(s)):
    if mae == 'R' and s[i] == 'R':
        countR += 1
    elif mae == 'L' and s[i] == 'L':
        countL += 1
    elif mae == 'R' and s[i] == 'L':
        s2.append(countR)
        countR = 1
    elif mae == 'L' and s[i] == 'R':
        s2.append(countL)
        countL = 1
    mae = s[i]

s2.append(countL)
now = 0

for i in range(1,len(s)):
    if s[i-1] == 'R' and s[i] == 'L':
        if (s2[now] + s2[now+1]) % 2 == 0:
            ans[i-1] += int((s2[now] + s2[now+1]) / 2)
            ans[i] += int((s2[now] + s2[now+1]) / 2)
        else:
            if s2[now] % 2 != 0:
                ans[i-1] += int((s2[now] + s2[now+1] + 1) / 2)
                ans[i] += int((s2[now] + s2[now+1] - 1) / 2)
            else:
                ans[i-1] += int((s2[now] + s2[now+1] - 1) / 2)
                ans[i] += int((s2[now] + s2[now+1] + 1) / 2)
        now += 2



print(' '.join(map(str, ans)))