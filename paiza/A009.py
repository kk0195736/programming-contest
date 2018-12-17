H, W = list(map(int, input().split()))

a = [[0 for i in range(W)] for i in range(H)]

for i in range(H):
    S = list(input())
    for j in range(len(S)):
        if S[j] == '\\':
            a[i][j] = 1
        elif S[j] == '/':
            a[i][j] = 2
        else:
            pass

now_x = 0
now_y = 0
counter = 0
direction = 1

#print(a)

while True:
    #print(counter, now_x, now_y, direction)
    if not (0 <= now_x < H and 0 <= now_y < W):
        #print(now_x, now_y, direction)
        print(counter)
        break
    else:
        if a[now_x][now_y] == 1:
            if direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 4
            else:
                direction =3

        elif a[now_x][now_y] == 2:
            if direction == 1:
                direction = 4
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 2
            else:
                direction = 1

        else:
            pass

        counter += 1

        if direction == 1:
            now_y += 1
        elif direction == 2:
            now_x += 1
        elif direction == 3:
            now_y -= 1
        else:
            now_x -= 1


        '''
        if direction == 1:
            if a[now_x+1][now_y] == 1:
                direction = 2
            if a[now_x+1][now_y] == 2:
                direction = 4
            now_x += 1
        elif direction == 2:
            if a[now_x][now_y+1] == 1:
                direction = 1
            if a[now_x][now_y+1] == 2:
                direction = 3
            now_y += 1
        elif direction == 3:
            if a[now_x-1][now_y] == 1:
                direction = 4
            if a[now_x-1][now_y] == 2:
                direction = 2
            now_x -= 1
        else:
            if a[now_x][now_y-1] == 1:
                direction = 3
            if a[now_x][now_y-1] == 2:
                direction = 1
            now_y -= 1
        '''
        '''
        print(now_x, now_y, direction)
        if direction == 1:
            if a[now_x+1][now_y] == 0:
                #print(now_x, now_y, direction)
                now_x += 1
                counter += 1
                print(now_x, now_y, direction)
            elif a[now_x+1][now_y] == 1:
                #print(now_x, now_y, direction)
                now_x += 1
                direction = 2
                counter += 1
                print(now_x, now_y, direction)
            else:
                #print(now_x, now_y, direction)
                now_y -= 1
                direction = 4
                counter += 1
                print(now_x, now_y, direction)
        elif direction == 2:
            if a[now_x][now_y] == 0:
                #print(now_x, now_y, direction)
                now_y += 1
                counter += 1
            elif a[now_x][now_y] == 1:
                #print(now_x, now_y, direction)
                now_x += 1
                direction = 1
                counter += 1
                print(now_x, now_y, direction)
            else:
                #print(now_x, now_y, direction)
                now_x -= 1
                direction = 3
                counter += 1
                print(now_x, now_y, direction)
            
        elif direction == 3:
            if a[now_x][now_y] == 0:
                #print(now_x, now_y, direction)
                now_x -= 1
                counter += 1
                print(now_x, now_y, direction)
            elif a[now_x][now_y] == 1:
                #print(now_x, now_y, direction)
                now_y -= 1
                direction = 4
                counter += 1
                print(now_x, now_y, direction)
            else:
                #print(now_x, now_y, direction)
                now_y += 1
                direction = 2
                counter += 1
                print(now_x, now_y, direction)
        else:
            if a[now_x][now_y] == 0:
                #print(now_x, now_y, direction)
                now_y -= 1
                counter += 1
                print(now_x, now_y, direction)
            elif a[now_x][now_y] == 1:
                #print(now_x, now_y, direction)
                now_x -= 1
                direction = 3
                counter += 1
                print(now_x, now_y, direction)
            else:
                #print(now_x, now_y, direction)
                now_x += 1
                direction = 1
                counter += 1
                print(now_x, now_y, direction)
        '''



#print(H, W, a)