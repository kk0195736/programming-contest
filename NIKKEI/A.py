N, A, B = map(int, input().split())

if A + B >= N:
    print(min(A, B), A + B - N)
else:
    print(min(A,B), 0)