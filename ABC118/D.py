N, M = list(map(int, input().split()))
A = list(map(str, input().split()))

li = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}


B = []

for i in A:
    if i == '1':
        B.append(2)
    elif i == '7':
        B.append(3)
    elif i == '4':
        B.append(4)
    elif i == '6' or i == '9':
        B.append(6)
    elif i == '8':
        B.append(7)
    else:
        B.append(5)

ans = []

if min(B) == 2:
    while True:
        
