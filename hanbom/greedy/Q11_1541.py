import sys, re
input=sys.stdin.readline
str_lst=re.split('([-|+])',input().strip())

cnt=0
n=0
positive=True
for idx in range(len(str_lst)):
    if str_lst[idx] == "-":
        # print(positive, n)
        if positive: cnt+=n
        else: cnt-=n
        positive= False
        n=0
    elif str_lst[idx] == "+":
        pass
    
    else: 
        n+=int(str_lst[idx])
        
    if idx==len(str_lst)-1:
        # print(positive, n)
        if positive: cnt+=n
        else: cnt-=n

print(cnt)