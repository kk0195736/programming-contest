import math


N, K = list(map(int, input().split()))

inf = 10**9 + 7

for i in range(K):
    blue = K - 1 - i
    red = N - K - i

    bluebox = i + 1
    redbox = i + 
    
    if bluebox == 1:
        b = 1
    else:
        b = 0
        if bluebox >= blue:
            co = blue
        else:
            
    if redbox == 1:
        r = 0
    else:
        r = 0

    print((b)*(r) % inf)
