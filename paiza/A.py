#import numpy as np

'''
def judge_empty(int_array):
    for i in int_array:
        if i != 0:
            return False
    return True

def set_block(height, width):
    pass
'''

def fill(hight, width, start_point):
    for i in range(hight):
        for j in range(width):
            


H, W, N = 7, 10, 1#list(map(int, input().split()))

h = []
w = []
x = []

for i in range(N):
    a, b, X = 2, 2, 1#list(map(int, input().split()))
    h.append(a)
    w.append(b)
    x.append(X)

a = [[0 for i in range(W)] for i in range(H)]

a[6, 1] = 1
for i in range(N):
    for j in range(H-h[i]):
        if not judge_empty(a[h[i]+j, x[i]:w[i]+1]):
            a[:h[i]+j, x[i]:w[i]+1] = 1
        if not judge_empty(a[h[i]+j, x[i]:w[i]+1]) and j == H-h[i]:
            a[:h[i]+j, x[i]:w[i]+1] = 1

print(a)



for i in range(H):
    for j in range(W):
        if a[i, j] == 0:
            print(".", end="")
        else:
            print("#", end="")
    print()
