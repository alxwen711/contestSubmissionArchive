import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
for a given subarray, there has to be two other subarrays that
could work

sliding windows can be possible
determine if a subarray is good by min/max check and unique val count

binary searching is NOT possible
"""

def create_seg(f,ar):
    seg = list()
    seg.append(ar)
    while len(seg[-1]) != 1:
        tmp = list()
        for i in range(len(seg[-1])//2):
            tmp.append(f(seg[-1][2*i],seg[-1][2*i+1]))
        seg.append(tmp)
    return seg

def query(f,seg,li,ri,sv):
    ans = sv
    l,r = li,ri
    for i in range(len(seg)):
        if l > r: return ans
        if l % 2 == 1:
            ans = f(ans,seg[i][l])
            l += 1
        if r % 2 == 0:
            ans = f(ans,seg[i][r])
            r -= 1
        l >>= 1
        r >>= 1
    return ans


def f(n,ar,x,minseg,maxseg):
    # setup 1st sliding window
    sega = [0]*(n+1)
    acount = 0
    for i in range(x-1):
        if sega[ar[i]] == 0: acount += 1
        sega[ar[i]] += 1
    for a in range(x-1,n-x):
        # add to get the length
        if sega[ar[a]] == 0: acount += 1
        sega[ar[a]] += 1
        if acount == x:
            # min/max check
            minv = query(min,minseg,a-x+1,a,99999999999999999)
            maxv = query(max,maxseg,a-x+1,a,-99999999999999999)
            if maxv-minv+1 == x:
                # a is valid, start iterating through b
                segb = {}
                bcount = 0
                for j in range(a+1,a+x):
                    if segb.get(ar[j],0) == 0:
                        segb[ar[j]] = 0
                        bcount += 1
                    segb[ar[j]] += 1
                for b in range(a+x,n):
                    # add to complete b subarray
                    if segb.get(ar[b],0) == 0:
                        segb[ar[b]] = 0
                        bcount += 1
                    segb[ar[b]] += 1
                    if bcount == x:
                        # min/max check with a conditional
                        min2v = query(min,minseg,b-x+1,b,99999999999999999)
                        if min2v == maxv+1:
                            if query(max,maxseg,b-x+1,b,-99999999999999999) == maxv+x: return True
                        if minv - x == min2v:
                            if query(max,maxseg,b-x+1,b,-99999999999999999) == minv-1: return True
                    # then subtract b-x+1
                    pos = b-x+1
                    segb[ar[pos]] -= 1
                    if segb[ar[pos]] == 0: bcount -= 1
        # remove a-x+1
        pos = a-x+1
        sega[ar[pos]] -= 1
        if sega[ar[pos]] == 0: acount -= 1
    return False

anslist = list()
for _ in range(readint()):
    n = readint()
    ar = readar()
    minseg = create_seg(min,ar)
    maxseg = create_seg(max,ar)
    if not f(n,ar,1,minseg,maxseg):
        anslist.append(0)
        continue
    for snth in range(n//2,0,-1):
        if f(n,ar,snth,minseg,maxseg):
            anslist.append(snth)
            break
sys.stdout.write("\n".join(map(str,anslist)))
