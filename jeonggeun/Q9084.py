import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coin = list(map(int,input().split()))
    M = int(input())

    dp = [0]*(M+1)
    dp[0] = 1
    for i in range(len(coin)):
        for j in range(1,M+1):
            if j >= coin[i]:
                dp[j] += dp[j-coin[i]]
    print(dp[M])