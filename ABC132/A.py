S = list(input())
s = set(S)

if len(s) == 2:
    a = S[0]
    count = 0
    for i in S:
        if i == a:
            count += 1

    if count == 2:
        print('Yes')
    else:
        print('No')

else:
    print('No')