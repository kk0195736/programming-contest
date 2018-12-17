N, X = list(map(int, input().split()))

a = [1]
p = [1]

for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)

def sou(level):
    if level == 0:
        return 1
    else:
        return sou(level - 1) * 2 + 3

def patty(N):
    if N == 0:
        return 1
    else:
        return patty(N-1) * 2 + 1

def dp(N, X):
    if N >= 2:
        if X == 1:
            return 0
        elif X <= 1 + sou(N-1):
            return dp(N-2, X-1)
        elif X == 1 + sou(N-1) + 1:
            return patty(N-1) + 1
        elif X <= 1 + sou(N-1) + 1 + sou(N-1):
            X = X - 1 - sou(N-1) - 1
            return patty(N-1) + 1 + dp(N-2, X)
        elif X == sou(N):
            return patty(N)
    else:
        if N == 0:
            return 1
        else:
            if X == 1:
                return 0
            elif X == 2:
                return 1
            elif X == 3:
                return 2
            else:
                return 3


print(dp(N, X))