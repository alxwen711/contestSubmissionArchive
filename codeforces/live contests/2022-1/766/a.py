import sys
for i in range(int(sys.stdin.readline())):
    r,c,x,y = map(int,sys.stdin.readline().split())
    whiteFlag = False
    rcCheck = False
    B = False
    for j in range(r):
        l = str(sys.stdin.readline())
        if l.count("B") != 0: whiteFlag = True
        if l[y-1] == "B": rcCheck = True
        if j+1 == x:
            if l.count("B") != 0: rcCheck = True
            if l[y-1] == "B":
                B = True
    if B: print(0)
    elif rcCheck: print(1)
    elif whiteFlag: print(2)
    else: print(-1)
