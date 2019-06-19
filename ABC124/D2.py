N, K = list(map(int, input().split()))

S = input()

k = K * 2 + 1

a = []
f = S[0]
l = S[-1]

count = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        count += 1
    else:
        a.append(count)
        count = 1
a.append(count)

ze = int(len(a)/2)

if f == '0' and len(a) % 2 != 0:
    ze += 1

if K >= ze:
    print(sum(a))
else:
    ans = 0
    if f == '1':
        if l == '1':
            for i in range(ze - K +1):
                if ans < sum(a[i*2:i*2+k]):
                    ans = sum(a[i*2:i*2+k])
        else:
            for i in range(ze - K +1):
                if i != ze - K:
                    if ans < sum(a[i*2:i*2+k]):
                        ans = sum(a[i*2:i*2+k])
                else:
                    if ans < sum(a[i*2:i*2+k-1]):
                        ans = sum(a[i*2:i*2+k-1])
    else:
        ans = sum(a[:k-1])
        if l == '1':
            for i in range(1,ze - K +1):
                if ans < sum(a[i*2:i*2+k]):
                    ans = sum(a[i*2:i*2+k])
        else:
            for i in range(1,ze - K +1):
                if i != ze - K:
                    if ans < sum(a[i*2:i*2+k]):
                        ans = sum(a[i*2:i*2+k])
                else:
                    if ans < sum(a[i*2:i*2+k-1]):
                        ans = sum(a[i*2:i*2+k-1])

    print(ans)