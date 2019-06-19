A, B, K = list(map(int, input().split()))

S = [1]

for i in range(2,min(A+1,B+1)):
    if A % i == 0 and B % i == 0:
        S.append(i)

S.sort(reverse=True)

print(S[K-1])