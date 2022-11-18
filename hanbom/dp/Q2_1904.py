"""
[문제] 백준2748-피보나치 수열2
시간제한 1초, 메모리 제한 128MB, n<=90

*입력
- 타일 개수
*출력
- 타일 입력값개를 사용한 가지수

[풀이]
1. 타일 n개에 대해서 타일 n-1과 타일 n-2를 사용한 가지수의 합과 같다. 즉 피보나치 수열이다.
2. 점화식 f[x]=f[x-1]+f[x-2]
3. dp 하향식 방식은 해당 조건에서 메모리를 너무 많이 차지한다.
4. 사향식을 사용해서 풀것
"""
import sys
# sys.setrecursionlimit(10**5)
input=sys.stdin.readline
x=int(input())

tile={
    0:0,
    1:1,
    2:2
}

def tileDP(x):
    for i in range(3,x+1):
        tile[i]=(tile[i-1]+tile[i-2])%15746
    return tile[x]

print(tileDP(x))

# ---- 시간초과 및 recursionError ----
#원인: 값이 큰 x에 대해서 함수값이 int를 초과하기 때문에 엄청 많은 메모리 차지를 하게된다.
# => 따라서 하향식으로 풀게 될 경우, 재귀를 사용하기 때문에 메모리 효율이 좋지 않다.
#해결: 하향식이 아닌 상향식으로 풀면 해결된다.
# tile={
#     0:0,
#     1:1,
#     2:2
# }

# def tileDP(x):
#     if x in tile:
#         return tile[x]
#     tile[x]=(tileDP(x-1)+tileDP(x-2))%15746
#     return tile[x]

# print(tileDP(x))