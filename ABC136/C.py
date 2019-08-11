N = int(input())
H = list(map(int, input().split()))

now = H[0] - 1

for i in range(1,N):
    if H[i] - now == 0:
        pass
    elif H[i] - now == 1:
        pass
    elif H[i] - now >= 2:
        now = H[i] - 1
    else:
        print('No')
        exit()

print('Yes')