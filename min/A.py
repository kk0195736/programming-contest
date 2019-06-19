N, K = list(map(int, input().split()))

if N % 2 == 0:
    if N / 2 >= K:
        print('YES')
    else:
        print('NO')

else:
    if (N + 1) / 2 >= K:
        print('YES')
    else:
        print('NO')