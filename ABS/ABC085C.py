N, Y = map(int, input().split())

def rec(i, j):
    if  i == 0 and j == 0:
        return print("True")
    else:
        if i == 0 and j != 0:
            return print("-1 -1 -1")
        else:
            if j >= 10000:
                
                return rec(i-1, j-10000)
            elif j >= 5000:
                
                return rec(i-1, j-5000)
            else:
                
                return rec(i-1, j-1000)

print(rec(N, Y))