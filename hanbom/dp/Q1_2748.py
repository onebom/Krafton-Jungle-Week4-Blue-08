"""
[문제] 백준2748-피보나치 수열2
시간제한 1초, 메모리 제한 128MB, n<=90

*입력
- 출력하고 싶은 피보나치 수열 index n
*출력
- index n 번째 피보나치 수열 값

[풀이]
1. fibo라는 메모리변수를 할당
2. 재귀함수를 통해 bottomUP 방식으로 n까지의 피보나치 수열 값 저장
"""
import sys
input=sys.stdin.readline

fibo={
    0:0,
    1:1
}

def fiboDP(x):
    if x in fibo:
        return fibo[x]

    fibo[x]=fiboDP(x-1)+fiboDP(x-2)
    return fibo[x]

print(fiboDP(int(input())))