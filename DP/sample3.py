def fib3(n):
    if n == 0:
        return 1
    else:
        fib1 = fib2 = fib3 = 1
        for i in range(n-1):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        return fib2

n = int(input())

print(fib3(n))