N = int(input())
A = list(map(int, input().split()))

A.sort()

max_pair = A[-1] + A[-2]
min_pair = A[0] + A[1]

for i in 