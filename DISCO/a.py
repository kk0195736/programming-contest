N = int(input())

k = int(N / 2) -1
for i in range(k):
    k += i

if N % 2 == 0:
    print(k * 4)

else:
    print(k*4 + 1)