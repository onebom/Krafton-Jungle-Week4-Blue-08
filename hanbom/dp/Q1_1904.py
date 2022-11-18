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