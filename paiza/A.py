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


def fill(hight, width, start_point_x, start_point_y):
    for i in reversed(range(start_point_y+1-hight, start_point_y+1)):
        for j in range(start_point_x, width+start_point_x):
            a[i][j] = 1


def judge_empty(witdth, start_point):
    m = H - 1
    for i in reversed(range(1, H)):
        for j in range(start_point, witdth+start_point):
            if a[i][j] == 1:
                m = i-1
                break
    return m


H, W, N = list(map(int, input().split()))

h = []
w = []
x = []

for i in range(N):
    a, b, X = list(map(int, input().split()))
    h.append(a)
    w.append(b)
    x.append(X)

a = [[0 for i in range(W)] for i in range(H)]

#a[6, 1] = 1
'''
for i in range(N):
    for j in range(H-h[i]):
        if not judge_empty(a[h[i]+j, x[i]:w[i]+1]):
            a[:h[i]+j, x[i]:w[i]+1] = 1
        if not judge_empty(a[h[i]+j, x[i]:w[i]+1]) and j == H-h[i]:
            a[:h[i]+j, x[i]:w[i]+1] = 1
'''
'''
print(a)

fill(2, 2, 1, 6)

fill(5, 2, 3, judge_empty(2, 3))

print(judge_empty(2, 1))
'''

for i in range(N):
    fill(h[i], w[i], x[i], judge_empty(w[i], x[i]))

for i in range(H):
    for j in range(W):
        if a[i][j] == 0:
            print(".", end="")
        else:
            print("#", end="")
    print()
