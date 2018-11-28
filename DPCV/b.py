N, K = map(int, input().split())

S = list(map(int, input().split()))

A = []

for i in range(N+1):
    for j in range(i):
        A.append(sum(S[j:i]))

A.sort()
A.reverse()

for i in range(len(A)):
        counter = 0
        ans = 0
        for j in range(len(A)):
                if A[i] & A[j] == A[i]:
                        counter += 1
                if counter == K:
                        ans = A[j]
                        break
        if ans != 0:
                break

print(ans)