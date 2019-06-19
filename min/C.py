K, A, B = list(map(int, input().split()))

if B - A <= 2:
    print(K + 1)

else:
    if K <= A:
        print(K + 1)
    else:
        bisket = 1
        K -= A - 1
        bisket += A - 1
        if K % 2 != 0:
            K -= 1
            bisket += 1
        bisket += (B - A) * int(K / 2)

        print(bisket)