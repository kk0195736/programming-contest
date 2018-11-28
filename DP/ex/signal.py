import math
N = 20
f0 = 2000
d = 1/40000


def x(i):
    if 0 <= i <= 9:
        return 1
    else:
        return 0

a, b = list([[0 for i in range(4)]for j in range(2)])

for n in range(4):
    for i in range(N):
        a[n] += x(i)*math.cos(2*math.pi*n*f0*i*d)
        b[n] += x(i)*math.sin(2*math.pi*n*f0*i*d)
        print("a[", n, "]=", a[n])
        print("b[", n, "]=", b[n])
