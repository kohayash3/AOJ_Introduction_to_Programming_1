W,H,x,y,r = map(int,input().split())
if x < r or x+r > W or y < r or y+r > H:
    print("No")
else:
    print("Yes")