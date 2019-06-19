N = int(input())
S = input()

while True:
    if S[-1] == '.':
        break
    if S[-1] == '#':
        s = list(S)
        del s[-1]
        S = ''.join(s)



print(min(S.count('.'),S.count('#')))