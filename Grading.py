while True:
    m,f,r = map(int,input().split())
    score = m + f
    if m == r == f == -1:
        break
    if score < 30 or m == -1 or f == -1:
        print("F")
        continue
    if score >= 80:
        print("A")
    if 65 <= score < 80:
        print("B")
    if 50 <= score < 65:
        print("C")
    if 30 <= score < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
  


