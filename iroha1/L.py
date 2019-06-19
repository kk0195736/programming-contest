N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

c = []

for i in A:
    s = str(format(i, 'b')).zfill(59)
    for i in 