N = int(input())

def dp(N):
    if True:
        pass
    else:
        if int(N % 10 ** (len(str(N)) - 1)) >= 7:
            pass
        elif int(N % 10 ** (len(str(N)) - 1)) >= 5:
            pass
            
        elif int(N % 10 ** (len(str(N)) - 1)) >= 3:
            pass
        else:
            pass

if N < 357:
    print(0)
elif N < 375:
    print(1)
elif N < 537:
    print(2):
elif N < 573:
    print(3)
elif N < 735:
    print(4)
elif N < 753:
    print(5)
elif N < 3357:
    print(6)
else:
    int(N / 1000)

ans = 0

for i in range(1,N):
    S = list(str(i))

    if ('7' in S) and ('5' in S) and ('3' in S):
        ans += 1

print(ans)