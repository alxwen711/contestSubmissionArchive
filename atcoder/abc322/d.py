import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def calc_dim(ar): #also get bits filled in
    ax,ay,bx,by = 5,5,-1,-1
    bc = 0
    for x in range(4):
        for y in range(4):
            if ar[x][y] == "#":
                bc += 1
                ax = min(ax,x)
                ay = min(ay,y)
                bx = max(bx,x)
                by = max(by,y)
    return bc,bx-ax+1,by-ay+1,ax,ay

def translations(ar,x,y,sx,sy):
    tr = list()
    for i in range(4-x+1):
        for j in range(4-y+1):
            br = list()
            for snth in range(4):
                tmp = ["."]*4
                br.append(tmp)
            for a in range(x):
                for b in range(y):
                    br[a+i][b+j] = ar[sx+a][sy+b]
            tr.append(br)
    return tr

def compute(ar):
    v = 0
    for i in range(4):
        for j in range(4):
            v *= 2
            if ar[i][j] == "#": v += 1
    return v

def rotate(ar): #90 deg cw rotation
    br = list()
    for i in range(4):
        cr = list()
        for j in range(4):
            cr.append(ar[3-j][i])
        br.append(cr)
    return br

ar = list()
br = list()
cr = list()
for aaa in range(4):
    s = input()
    ar.append(s)
for bbb in range(4):
    s = input()
    br.append(s)
for ccc in range(4):
    s = input()
    cr.append(s)

# get dimensions
ac,ax,ay,asx,asy = calc_dim(ar)
bc,bx,by,bsx,bsy = calc_dim(br)
cc,cx,cy,csx,csy = calc_dim(cr)
if (ac+bc+cc) != 16: print("No")
else:
    #translation values
    aar = translations(ar,ax,ay,asx,asy)
    bbr = translations(br,bx,by,bsx,bsy)
    ccr = translations(cr,cx,cy,csx,csy)

    #evaluation points
    av = list()
    bv = list()
    cv = list()
    for a in aar:
        av.append(compute(a))
        a = rotate(a)
        av.append(compute(a))
        a = rotate(a)
        av.append(compute(a))
        a = rotate(a)
        av.append(compute(a))
    for b in bbr:
        bv.append(compute(b))
        b = rotate(b)
        bv.append(compute(b))
        b = rotate(b)
        bv.append(compute(b))
        b = rotate(b)
        bv.append(compute(b))
    for c in ccr:
        cv.append(compute(c))
        c = rotate(c)
        cv.append(compute(c))
        c = rotate(c)
        cv.append(compute(c))
        c = rotate(c)
        cv.append(compute(c))
    ans = "No"
    for aa in av:
        for bb in bv:
            for cc in cv:
                if (aa & bb == 0) and (bb & cc == 0) and (aa & cc == 0) and (aa | bb | cc == (2**16)-1):
                    ans = "Yes"
    print(ans)
