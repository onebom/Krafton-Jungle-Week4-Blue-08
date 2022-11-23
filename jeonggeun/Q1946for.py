import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    table = [0]*N
    count = 1
    for _ in range(N):
        a, b = map(int, input().split())
        table[a-1] = b
    cutline = table[0]
    for i in range(1,N):
        if cutline < table[i]:
            continue
        else:
            count += 1
            cutline = table[i]
    print(count)