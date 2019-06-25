W, H, x, y = list(map(int, input().split()))

ans = W*H/2

flag = 0


if W/2 == x and H/2 == y:
    flag = 1


print(ans,flag)