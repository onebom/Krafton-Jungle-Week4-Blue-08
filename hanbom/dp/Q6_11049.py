import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n=int(input)
mt=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]

for i in range(1,n):
    for j in range(n-i):
        x=i+j
        dp[j][x]=2**32
        for k in range(j,x):
            dp[j][x]=min(dp[j][x], dp[j][k]+dp[k+1][x]+mt[j][0]*mt[k][1]*mt[x][1])

print(dp[0][n-1])