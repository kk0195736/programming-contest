f = [0 for i in range(10000)]

def fib2(n):
    if n <= 1:
        return 1
    else:
        if f[n] != 0:
            return f[n]
        else:
            f[n] = fib2(n-1) + fib2(n-2)
            return f[n]

n = int(input())

print(fib2(n))