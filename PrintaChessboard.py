while True:
    H,W = map(int,input().split())
    if H == W == 0:
        break
    for i in range(H):
        if i == 0 or i == H:
            print("#"*W)
