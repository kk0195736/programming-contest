N = int(input())

A = list(map(int, input().split()))

for i in range(N):
    c = 0
    while True:
        if A[i] % 2 == 1:
            A[i] = c
            break
        else:
            A[i] = int(A[i] / 2)
            c +=1

print(min(A))