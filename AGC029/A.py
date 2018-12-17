S = input()

counter = 0
arr = list(S)

def TurnOver(arr):
    for i in range(len(arr)):
        Consecutive_B = 0
        if arr[i] == 'B':
            for j in range(i, len(arr)):
                Consecutive_W = 0
                if arr[j] == 'W':
                    for k in range(j, len(arr)):
                        if arr[k] == 'B' or k == (len(arr) - 1):
                            return Consecutive_B * Consecutive_W
                        Consecutive_W += 1
                        arr[k] = 'B'
                Consecutive_B += 1
                arr[j] = 'W'
    return 0

def TurnOver2(arr):
    for i in range(len(arr)):
        if arr[i] == 'B':
            for j in range(i, len(arr)):
                if arr[j] == 'W':
                    for k in range(j, len(arr)):
                        if arr[k] == 'B' or k == (len(arr) - 1):
                            break
                        arr[k] = 'B'
                arr[j] = 'W'
    return 0

while True:
    if TurnOver(arr) > 0:
        counter += TurnOver(arr)
        TurnOver2(arr)
    else:
        break

print(counter)