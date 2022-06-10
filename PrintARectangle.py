while True:
    H,W = map(int,input().split())
    if H == W == 0:
        break
    for i in range(H):
        w_block = W // 2
        w_rem = W % 2
        if i % 2 == 0: #その行が奇数の場合
            print("#."*w_block,"#"*w_rem,sep="")
        else:
            print(".#"*w_block,"."*w_rem,sep="")
        i += 1
    print()