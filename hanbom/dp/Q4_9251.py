import sys
input=sys.stdin.readline

a=list(input().strip())
b=list(input().strip())
if len(a)<len(b):
    a,b=b,a
str_dp=[0]*(len(b)+1)

print(a,b)

start=0
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]:
            if str_dp[j]+1 <= i+1:
                str_dp[j+1]=str_dp[j]+1
            else: 
                str_dp[j+1]=str_dp[j]
        else:
            str_dp[j+1]=max(str_dp[j+1], str_dp[j])
            
        print(str_dp)

print(str_dp[-1])