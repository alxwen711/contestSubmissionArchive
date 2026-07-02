import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readar = lambda: list(map(int,sys.stdin.readline().split()))


def create_seg(f,ar):
    seg = list()
    seg.append(ar)
    dist = 2
    n = len(seg[0])
    while dist <= n:
        tmp = [0]*(n-dist+1)
        for i in range(n-dist+1):
            tmp[i] = f(seg[-1][i],seg[-1][i+dist//2])
        seg.append(tmp)
        dist *= 2
    return seg

def query(f,seg,li,ri):
    dist = ri-li+1
    index = 0
    c = 1
    while c*2 < dist:
        c <<= 1
        index += 1
    return f(seg[index][li],seg[index][ri-c+1])

def f(n,ar,x,minseg,maxseg):
    # setup 1st sliding window
    sega = [0]*(n+1)
    acount = 0
    lowdict = [9999]*(n+1)
    highdict = [-9999]*(n+1)
    for i in range(x-1):
        if sega[ar[i]] == 0: acount += 1
        sega[ar[i]] += 1
    for a in range(x-1,n):
        # add to get the length
        if sega[ar[a]] == 0: acount += 1
        sega[ar[a]] += 1
        if acount == x:
            # min/max check
            minv = query(min,minseg,a-x+1,a)
            maxv = query(max,maxseg,a-x+1,a)
            if maxv-minv+1 == x:
                # a is valid, record this setup somewhere
                lowdict[minv] = min(lowdict[minv],a)
                highdict[minv] = a
        # remove from the thing
        pos = a-x+1
        sega[ar[pos]] -= 1
        if sega[ar[pos]] == 0: acount -= 1
        
    for l in range(n+1):
        v = lowdict[l]
        if l > x and highdict[l-x] >= v+x: return True
        if l+x <= n and highdict[l+x] >= v+x: return True
    return False
                
          

anslist = list()
for _ in range(readint()):
    n = readint()
    ar = readar()
    minseg = create_seg(min,ar)
    maxseg = create_seg(max,ar)
    ans = 0
    for snth in range(n//2,0,-1):
        if f(n,ar,snth,minseg,maxseg):
            ans = snth
            break
    anslist.append(ans)
sys.stdout.write("\n".join(map(str,anslist)))
