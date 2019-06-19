S = input()
K = int(input())

K = K % len(S)

a = S[:K]
b = S[K:]

print(b+a)