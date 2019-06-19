N, X, Y = list(map(int, input().split()))
A = list(map(int,input().split()))

A.sort(reverse=True)
Ta = []
Ao = []

for i in range(N):
    if i % 2 == 0:
        Ta.append(A[i])
    else:
        Ao.append(A[i])

anst = sum(Ta) + X
ansa = sum(Ao) + Y

if anst == ansa:
    print('Draw')
elif anst > ansa:
    print('Takahashi')
else:
    print('Aoki')