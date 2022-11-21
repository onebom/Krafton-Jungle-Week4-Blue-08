import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    cdd_lst=[list(map(int,input().split())) for _ in range(n)]    
    cdd_lst.sort()
    
    cnt=t2_best=0
    for t1,t2 in cdd_lst:
        if t1==1 or t2<t2_best:
            t2_best=t2   
            cnt+=1
    
    print(cnt)

    


