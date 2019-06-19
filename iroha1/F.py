import math
#試し割法
def trial_division(n):
    #素因数を格納するリスト
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    #リストが空ならそれは素数
    if not factor:
        return [n]
    else:
        factor.append(n)
        return factor

N, K = list(map(int, input().split()))

A = trial_division(N)
A.sort()
if A[0] == 1:
    del A[0]


if len(A) < K:
    print(-1)
else:
    while True:
        if len(A) == K:
            break
        tmp = A[-1] * A[-2]
        del A[-1]
        del A[-1]
        A.append(tmp)

    print(*A)