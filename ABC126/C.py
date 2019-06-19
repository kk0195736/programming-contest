N, K = list(map(int, input().split()))

if N >= K:
    ans2 = (1/N) * (N - K+1)
    now = 1
    count = 0
    while True:
        if now >= K:
            break
        now *= 2
        count += 1

    ans = (1/N) * ((0.5) ** (count))

    A = [ans]

    for i in range(1,K):
        A.append(A[i-1]*2)
    print(sum(A)+ans2)
else:
    now = N
    count = 0
    while True:
        if now >= K:
            break
        now *= 2
        count += 1

    ans = (1/N) * ((0.5) ** count)

    A = [ans]

    for i in range(1,N):
        A.append(A[i-1]*0.5)

    print(sum(A))