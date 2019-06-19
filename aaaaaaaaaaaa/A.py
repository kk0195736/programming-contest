import math
N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

print(math.ceil(sum(A) / T))