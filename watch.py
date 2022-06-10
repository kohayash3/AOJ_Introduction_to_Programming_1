

# def div60(int):
#     tmp = int/60
#     return(tmp)

def check_h(int):
    h = 0
    if int >= 3600:
        h = int//3600
        remain = int - 3600*h
        return(h,remain)
    else:
        return(h,int)

def check_m(int):
    m = 0
    if int >= 60:
        m = int//60
        remain = int - 60*m
        return(m,remain)
    else:
        return(m,int)

def main():
    a = int(input())
    h, remain1 = check_h(a)
    m, s = check_m(remain1)
    print(str(h),":",str(m),":",str(s),sep="")

main()


# #より賢く
# S = int(input())
# print(S//3600,":",(S%3600)//60,":",S%60,sep="")
