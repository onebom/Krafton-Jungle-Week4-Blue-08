import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]
coin.reverse()
count = 0

for i in coin:
    if K >= i:
        count += K//i
        K %= i

print(count)