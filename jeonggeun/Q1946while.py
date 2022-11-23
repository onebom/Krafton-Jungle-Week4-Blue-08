import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    passed = [1]*N
    table = [tuple(map(int,input().split())) for _ in range(N)]
    table.sort()
    s = 0
    while s < N-1 and passed[N-1]:
        for i in range(s+1, N):
            if table[s][1] < table[i][1]:
                passed[i] = 0
            else:
                s = i
                break
    print(sum(passed))