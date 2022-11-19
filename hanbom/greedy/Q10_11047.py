import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]

cnt=0
for i in range(1,len(coin)+1):
    if k-coin[-i]<0:
        continue
    else:
        cnt+=k//coin[-i]
        k%=coin[-i]
        if k==0:
            break
        
print(cnt)
