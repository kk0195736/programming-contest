N,A,B,C,D = list(map(int, input().split()))

S = input()

if C < D:
    s = []
    for i in range(N):
        s.append(S[i])

    for i in range(1,C):
        if s[i] == '#' and s[i-1] == '#':
            print('No')
            exit()
    print('Yes')

else:
    s1 = []
    for i in range(N):
        s1.append(S[i])
    for i in range(1,C):
        if s1[i] == '#' and s1[i-1] == '#':
            print('No')
            exit()
    flag = False
    for i in range(B+1,D):
        if s1[i] == '.' and s1[i-1] == '.' and s1[i-2] == '.':
            flag = True
        
    if flag == True:
        print('Yes')
    else:
        print('No')