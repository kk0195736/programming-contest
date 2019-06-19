S = input()

if len(S) <= 2:
    print(0)

else:
    ans1 = 0
    ans2 = 0
    flag1 = 0
    flag2 = 1
    for i in S:
        if flag1 % 2 == int(i):
            pass
        else:
            ans1 += 1
        flag1 += 1
    for i in S:
        if flag2 % 2 == int(i):
            pass
        else:
            ans2 += 1
        flag2 += 1

    print(min(ans1,ans2))