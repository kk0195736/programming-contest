def counter(number):
    for i in range(1,number+1):
        yield i

N = int(input())

for i in counter(N):
    print(i)