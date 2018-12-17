S = list(input())

ans = 10000

for i in range(len(S)-2):
    if ans > abs(753 - int(S[i]+S[i+1]+S[i+2])):
        ans = abs(753 - int(S[i]+S[i+1]+S[i+2]))

print(ans)