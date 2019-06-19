H, W = list(map(int, input().split()))

h, w = list(map(int, input().split()))

H -= h
W -= w

print(H*W)