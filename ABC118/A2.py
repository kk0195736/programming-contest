A, B, C = list(map(int, input().split()))

if B >= A * C:
    print(C)
else:
    print(int(B / A))
