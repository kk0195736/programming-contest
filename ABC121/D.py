A, B = list(map(int, input().split()))

S = [False]*40

while True:
    if A == (B + 1):
        break
    s = str(bin(A))
    s = s[::-1]
    s = s[:-2]
    for i in range(len(s)):
        if s[i] == '1':
            if S[i] == False:
                S[i] = True
            else:
                S[i] = False
    A += 1

ans = []

for i in S:
    if i == True:
        ans.append('1')
    else:
        ans.append('0')

ans = ans[::-1]

ans = ''.join(ans)

print(int(ans, 2))