from collections import Counter

N = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 7]

S = Counter(N)

print(S[5])
print(N.count(5))