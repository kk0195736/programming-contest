import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

S = [A,B,C,D,E]

ans = math.ceil(N/min(S))

print(ans+4)