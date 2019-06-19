N = int(input())
h = list(map(int, input().split()))

ans_array = [h[0]]

i = 0

while True:
    if i >= N - 5:
        break

    a = abs(h[i] - h[i+1])
    b = abs(h[i] - h[i+2])
    c = abs(h[i+1] - h[i+2])
    d = abs(h[i+1] - h[i+3])
    e = abs(h[i+2] - h[i+3])
    f = abs(h[i+2] - h[i+4])

    p1 = a + c
    p2 = a + d

    p3 = b + e
    p4 = b + f

    if min(p1, p2, p3, p4) == p1:
        i += 1
        ans_array.append(h[i])
    elif min(p1, p2, p3, p4) == p2:
        i += 1
        ans_array.append(h[i])
    elif min(p1, p2, p3, p4) == p3:
        i += 2
        ans_array.append(h[i])
    else:
        i += 2
        ans_array.append(h[i])

if i == N - 4:
    pa1 = abs(h[i] - h[i+1]) + abs(h[i+1] - h[i+3])
    pa2 = abs(h[i] - h[i+2]) + abs(h[i+2] - h[i+3])

    if pa1 <= pa2:
        i += 1
        ans_array.append(h[i])
    else:
        i += 2
        ans_array.append(h[i])

ans = 0

ans_array.append(h[-1])

for i in range(len(ans_array)):
    if i == len(ans_array) - 1:
        break

    ans += abs(ans_array[i] - ans_array[i+1])

print(ans)
print(ans_array)