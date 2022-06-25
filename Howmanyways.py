# from re import I


# n,x = map(int,input().split())
# count = 0
# i=1
# j=1
# k=1
# while i <= x:
#     if n == x == 0:
#         break
#     for j in range(x-i):
#         for k in range (x-i-j):
#             if x == i+j+k:
#                 count+=1
    
# print(count)

while True:
    n,x = map(int,input().split())
    if n == x == 0:
        break
    cnt = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            if j < x-i-j <=n:
                cnt+=1
    print(cnt)