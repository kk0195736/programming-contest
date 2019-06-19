N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

a = []

for i in A:
    x = format(i, 'b')
    
    a.append(list(str(x.zfill(40))))

at = list(map(list, zip(*a)))

k = format(K, 'b')

print(len(k))
print(at)