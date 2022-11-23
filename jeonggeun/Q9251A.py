import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

matrix = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])

print(matrix[-1][-1])