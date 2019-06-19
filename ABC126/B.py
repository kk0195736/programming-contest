S = input()
s = []

for i in range(4):
    s.append(S[i])

mon = int(s[2] + s[3])
yer = int(s[0] + s[1])

if 1 <= mon <= 12:
    if 1 <= yer <= 12:
        print('AMBIGUOUS')
    else:
        print('YYMM')
else:
    if 1 <= yer <= 12:
        print('MMYY')
    else:
        print('NA')