S = input()

steps = 0
accumulated_W = 0

for i, x in enumerate(list(S)):
    if x == 'W':
        steps += i - accumulated_W
        accumulated_W += 1

print(steps)