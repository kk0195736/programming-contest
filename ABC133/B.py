import numpy as np

N, D = list(map(int, input().split()))

X = []
ans = 0

for i in range(N):
    x = list(map(int, input().split()))
    X.append(x)

np_X = np.array(X)


for i in range(1, N):
    for k in range(i,N):
        a = np_X[(i-1),:] - np_X[k,:]
        ad = 0
        for j in a:
            ad += j**2
        if np.sqrt(ad) - int(np.sqrt(ad)) == 0:
            ans += 1

print(ans)