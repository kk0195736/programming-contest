N = int(input())
A = input()
B = input()
C = input()

a = list(A)
b = list(B)
c = list(C)

ans = 0

for i,j in enumerate(a):
    if j == b[i] or j == c[i] or b[i] == c[i]:
        if j == b[i] == c[i]:
            continue
        ans += 1
    elif a[i] != b[i] != c[i]:
        ans += 2
    

print(ans)