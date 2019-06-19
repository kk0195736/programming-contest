R, G, B, N = list(map(int, input().split()))

r = int(N / R)
g = int(N / G)
b = int(N / B)

mi = min(r,g,b)

print((mi+1)*((b+1)/2))