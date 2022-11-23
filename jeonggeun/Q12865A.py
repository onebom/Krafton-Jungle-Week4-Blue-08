import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = dict()
d[0] = 0

for _ in range(N):
    tmp = []
    W, V = map(int, input().split())
    for key, value in d.items():
        if W + key <= K:
            tmp.append((W + key, V + value))
    for key, value in tmp:
        d.setdefault(key, 0)
        d[key] = max(d[key], value)
print(max(d.values()))