A, B, C = list(map(int, input().split()))

ans = B+C-A

if ans >= 0:
    print(ans)
else:
    print(0)