import sys
input = sys.stdin.readline
N = int(input())
table = [tuple(map(int,input().split())) for _ in range(N)]
table.sort(key = lambda x: (x[1],x[0]))

maxtable = 1
end_time = table[0][1]

for i in range(1,N):
    if table[i][0] >= end_time:
        maxtable += 1
        end_time = table[i][1]

print(maxtable)