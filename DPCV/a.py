N = int(input())

S = list(map(int, input().split()))

a = 10000

min = 0

for i in range(N):
    if abs(S[i] - sum(S)/len(S)) < a:
        a = abs(S[i] - sum(S)/len(S))
        min = i

print(min)