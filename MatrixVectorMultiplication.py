n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
B = [int(input()) for _ in range(m)]
for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j]*B[j]
    print(sum)