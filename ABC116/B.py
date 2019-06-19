S = int(input())

ans = 0

a = [S]

while True:
    ans += 1
    if a[ans - 1] % 2 == 0:
        an = a[ans - 1] / 2
    else:
        an = a[ans - 1] * 3 + 1
    if an in a:
        break
    a.append(an)

print(ans + 1)