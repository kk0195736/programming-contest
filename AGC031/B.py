N = int(input())

C = ''
a = 10 ** 9 + 7

for i in range(N):
    C += input()

ans = [C]

while True:
    b = len(set(ans))
    for i in ans:
        for j in i:


    if b == len(set(ans)):
        break

print(len(set(ans)))