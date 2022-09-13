import sys

"""def solve(ar,z,l):
    if z == 0 or z == l: return 0
    best = z
    point = 0
    fb = 99999999
    fbzero = 0
    fbone = 0
    fone = 0
    #forward search
    for a in range(z):
        fone += (ar[a]-point)
        front = max(fone,z-a-1)
        if front < fb:
            fb = front
            fbzero = z-a-1
            fbone = fone
        point = ar[a]+1

    #backward search
    point = l-1
    bb = 9999999999
    bbzero = 0
    bbone = 0
    bone = 0
    for b in range(z):
        bone += (point-ar[-b-1])
        back = max(bone,z-b-1)
        if back < bb:
            bb = back
            bbzero = z-b-1
            bbone = bone
        point = ar[-b-1]-1
    #if fb >= best and bb >= best: return best #no remove is better
    best = min(fb,bb)
    ans = best
    #print(fb,bb)
    if fb > -1:
        point = l-1
        fone = fbone
        for c in range(fbzero):
            fone += (point-ar[-c-1])
            subans = max(fone,fbzero-c-1)
            if subans < fb: fb = subans
            point = ar[-c-1]-1
        if fb < ans: ans = fb
    if bb > -1:
        point = 0
        bone = bbone
        for d in range(bbzero):
            bone += (ar[d]-point)
            subans = max(bone,bbzero-d-1)
            if subans < bb: bb = subans
            point = ar[d]+1
        if bb < ans: ans = bb
    return min(ans,z,l-z)
"""
for i in range(int(sys.stdin.readline())):
    x = str(sys.stdin.readline())[:-1]
    #ar = list()
    zero = 0
    xx = len(x)
    a = [0]*(xx+1)
    b = [0]*(xx+1)
    aa = [0]*(xx+1)
    bb = [0]*(xx+1)
    run = 0
    ones = 0
    for j in range(xx):
        if x[j] == "0":
            zero += 1
            run += 1
        else: ones += 1
        a[j+1] = run
        aa[j+1] = ones
    run = 0
    ones = 0
    for k in range(xx):
        if x[-k-1] == "0":
            run += 1
        else: ones += 1
        b[k+1] = run
        bb[k+1] = ones

    ans = zero
    #score = max(zero-a[j]-b[k],aa[j]+bb[k])
    #find the optimal j and k
    #section below is O(n^2), needs to be O(n log n) at least
    for e in range(xx+1):
        for f in range(xx-e+1):
            score = max(zero-a[e]-b[f],aa[e]+bb[f])
            if score < ans: ans = score
    print(ans)

    #print(solve(ar,zero,xx))
    """best = zero
    arf,arb = 0,xx-1
    fp = 0
    bp = len(ar)-1
    ones = 0
    for k in range(zero):
        fo,bo = ar[fp]-arf,arb-ar[bp]
        if fo < bo:
            ones += fo
            arf = ar[fp]+1
            fp += 1
        elif bo < fo:
            ones += bo
            arb = ar[bp]+1
            bp -= 1
        else: #tie scenario
            tiebreak = 1
            f = -1
            while True:
                if fp+tiebreak
                foo,boo = ar[fp+tiebreak]-arf, arb-ar[bp-tiebreak]

            
        if max(ones,zero-k-1) < best: best = max(ones,zero-k-1)
    print(best)
"""        
