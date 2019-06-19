N = int(input())

h = list(map(int, input().split()))

ans = 0

while True:
    if not any(h):
        break
    flag = False
    for i, e in enumerate(h):
        if e != 0:
            flag = True
            h[i] -= 1
            if i == len(h) - 1:
                ans += 1
        else:
            if flag == True:
                ans += 1
                flag = False
    
print(ans)