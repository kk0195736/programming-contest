MOD = 1000000007

if __name__ == "__main__":
    N = int(input())

    ans = 0

    for i in range(1, N+1):
        ans += (i ** 10 - (i - 1) ** 10) * (int(N / i) ** 10)
    
    print(ans % MOD)