from audioop import maxpp
import sys
input=sys.stdin.readline

n=int(input())
time=[list(map(int,input().split())) for _ in range(n)]

time.sort(key= lambda x: (x[1],x[0]))

print(time)
cnt=1
end_time=time[0][1]
for i in range(1,n):
    if time[i][0]>=end_time:
        cnt+=1
        end_time=time[i][1]

print(cnt)

#---------시간초과---------
# meet_lst=[]
# max_num=0
# for _ in range(n):
#     s,e=map(int,input().split())
#     max_num=max(max_num,e)
#     meet_lst.append([s,e])
    
# meet_lst.sort()
# meet=[0]*max_num

# for s,e in meet_lst: # 반복문 시작
#     if s>0:
#         meet[e-1]=max(meet[:s])+1 

#print(meet)
#print(max(meet))
    