import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
each q must be determined in O(log n) time? 5 second time limit is strange
if the value is some power of 2 that is large enough, it will go through all

maybe something with intervals? then once there's under 2**15 intervals the
remaining values should be brute forcable

if you are playing on same number of bits (suppose 0 to 15:)
8 into 8 is impossible
8 into 4 into 4 is impossible
4 into 8 into 4 is possible (11)

3 cases:
slime hits a higher bit power: impossible
slime hits an equal bit power: might be possible, seg tree compute value then
recalculate new bit power
slime hits a lower bit power: possible, use seg tree to speed up here
"""


def create_seg2(ar):
    br = list()
    br.append(ar)
    while len(br[-1]) != 1:
        cr = list()
        for i in range(len(br[-1])//2):
            cr.append(max(br[-1][2*i],br[-1][2*i+1]))
        br.append(cr)
    return br



def query(ar,low,high):
    ans = 0
    li,hi = low,high
    for i in range(len(ar)):
        if li > hi: return ans
        if li % 2 == 1:
            ans = max(ans,ar[i][li])
            li += 1
        if hi % 2 == 0:
            ans = max(ans,ar[i][hi])
            hi -= 1
        li >>= 1
        hi >>= 1
    return ans

def findexponent(vseg,index,n,xp):
    low = index
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if query(vseg,index,mid) < xp: low = mid
        else: high = mid
    if query(vseg,index,high) < xp: return high
    if query(vseg,index,low) < xp: return low
    return -1


for _ in range(readint()):
    n,q = readints()
    ar = readar()
    ar.reverse()
    vr = list()
    xseg = [0]
    for i in ar:
        vr.append(len(str(bin(i)))-2)
        xseg.append(xseg[-1]^i)
    
    
    vseg = create_seg2(vr)
    ansl = list()
    d = {}
    for _ in range(q):
        x = readint()
        if d.get(x) != None:
            ansl.append(d[x])
            continue
        basex = x
        xp = 0
        vv = 2
        while x >= vv:
            xp += 1
            vv *= 2
        ans = 0
        while ans != n:
            index = findexponent(vseg,ans,n,xp)
            if index != -1:
                x ^= xseg[ans]
                index += 1
                x ^= xseg[index]
                ans = index
            else: index = ans
            if ans == n: break

            # index challenging has been found
            if ar[index] > x: break
            else:
                x ^= ar[index]
                ans += 1
                
                xp = len(str(bin(x)))-2
                
        ansl.append(ans)
        d[basex] = ans
    print(*ansl)
