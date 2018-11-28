a = []
for i in range(29):
    A = int(input())
    a.append(A)

def henkan(X, n):
    if (int(X/n)):
        return henkan(int(X/n), n)+str(X%n)
    return str(X%n)


#print(sum(list(map(int,list(henkan(N, n))))))