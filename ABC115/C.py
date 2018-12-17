N, K = list(map(int, input().split()))

h = []

for i in range(N):
    H = int(input())
    h.append(H)

h.sort()

m = 9999999999999999999

for i in range(len(h)-K+1):
    if m > (h[i+K-1] - h[i]):
        m = (h[i+K-1] - h[i])

print(m)