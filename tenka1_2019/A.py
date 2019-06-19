A, B, C = list(map(int, input().split()))

if min(A,B) <= C and max(A,B) > C:
    print('Yes')
else:
    print('No')