N = int(input())
h = list(map(int, input().split()))

one_hop = []
two_hop = []

for i in range(1,N):
    one_hop.append(abs(h[i] - h[i-1]))

for i in range(2,N):
    two_hop.append(abs(h[i] - h[i-2]))

print(h)
print(one_hop)
print(two_hop)