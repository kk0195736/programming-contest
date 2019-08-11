N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

for i in range(N):
    if i == 0:
        print(max(A[1:]))
    elif i == N-1:
        print(max(A[:N-1]))
    else:
        print(max(max(A[:i]),max(A[i+1:])))
