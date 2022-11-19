"""
[문제] 백준9084-동전
시간제한 1초, 메모리제한 128MB
*입력
- 테스트 케이스(T), 동전가지수(N<=20)
- 가지수 만큼의 동전 금액(Ai<=10,000) => 같은 금액의 동전이 주어지지는 않음
- 만들어야 하는 금액(1<=M<=10,000)
*출력
- N가지 동전으로 금액 M을 만드는 가지수 
(ex) 5원,7원 => 22원 : 1가지)
"""
import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def coinDP(x,coin_idx):
    coin=coin_lst[coin_idx]
    # print(x, coin)
    if coin_idx==len(coin_lst)-1:
        if x%coin==0:
            return 1
        else:
            return 0
    else:
        # print("hi")
        rst=0
        while x>=0:
            rst+=coinDP(x,coin_idx+1)
            x-=coin
        return rst
    

for _ in range(int(input())):
    n=int(input())
    coin_lst=list(map(int,input().split()))
    m=int(input())
    
    coin_lst.sort(reverse=True)
    case_num=coinDP(m,0)
    print(case_num)