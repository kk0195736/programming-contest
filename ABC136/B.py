N = int(input())

if N <= 9:
    print(N)
elif 10 <= N and N <= 99:
    print(9)
elif 100 <= N and N <= 999:
    print(9+N-100+1)
elif 1000 <= N and N <= 9999:
    print(9+900)
elif 10000 <= N and N <= 99999:
    print(9+900+N-10000+1)
else:
    print(9+900+90000)
