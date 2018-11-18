N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

K = abs(A - (T - H[0] * 0.006))
x = 0
ans = 0

for i in H:
    x += 1
    if K >= abs(A - (T - i * 0.006)):
        K = abs(A - (T - i * 0.006))
        ans = x

print(ans)