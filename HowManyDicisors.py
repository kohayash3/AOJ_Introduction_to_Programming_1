a,b,c = map(int,input().split())
count = 0
for i in range(a,b+1):
    cal = c/i
    if(cal.is_integer()==True):
        count+=1
    i+=1
print(count)

# #あまりが0かどうかで判定するやり方もあり
# a,b,c=map(int,input().split())
# cnt=0
# for k in range(a,b+1):
#     if c%k==0:
#         cnt+=1
# print(cnt)