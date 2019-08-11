inf = float('inf')
print(inf)
'''
N = int(input())
h = list(map(int, input().split()))

DP = []

for i in range(N):
    if i == 0:
        DP.append(0)
    elif i == 1:
        DP.append(abs(h[0] - h[1]))
    else:
        one_hop = abs(h[i-1] - h[i]) + DP[i-1]
        two_hop = abs(h[i-2] - h[i]) + DP[i-2]
        if one_hop <= two_hop:
            DP.append(one_hop)
        else:
            DP.append(two_hop)

print(DP[-1])
'''