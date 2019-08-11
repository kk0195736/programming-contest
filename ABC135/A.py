A, B = list(map(int, input().split()))

ab = int(abs(A-B)/2)

if (A % 2 != 0 and B % 2 == 0) or (A % 2 == 0 and B % 2 != 0):
    print("IMPOSSIBLE")
else:
    print(min(abs(A), abs(B))+ab)