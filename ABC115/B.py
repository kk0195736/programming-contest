N = int(input())

p = []

for i in range(N):
    P = int(input())
    p.append(P)

max = 0

for i in p:
    if max <= i:
        max = i

print(int(sum(p) - max/2))