import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
max dimensions is 200k x 200k, naive seg tree ideas can't be done here
O(n sqrt(n)) ideas exist but they don't seem fast enough
either that or they have to be VERY optimized (only one pass allowed)
is O(n sqrt(n)) memory too much?
"""

def condense(br,m,intervals,l,r):
    ar = list()
    for i in range(l,r):
        ar.append((intervals[i][0],1))
        ar.append((intervals[i][1]+1,-1))
    ar.sort()
    ptr = 0
    #br = list()
    v = 0
    for j in range(1,m+1):
        while ptr != len(ar):
            if ar[ptr][0] == j:
                v += ar[ptr][1]
                ptr += 1
            else: break
        br[j-1] = v
        
def create_supergrid(nn,m,v,intervals):
    if nn < v: return [0]
    ar = [0]*m
    n = nn//v
    grid = list()
    for _ in range(n+1):
        tmp = [0]*(m+1)
        grid.append(tmp)
    for i in range(1,n+1):
        condense(ar,m,intervals,i*v-v,i*v)
        for j in range(1,m+1):
            grid[i][j] = ar[j-1]+grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
    return grid

def compute(grid,a,b,c,d):
    # row a to row b, col c to col d
    return grid[b+1][d+1]-grid[a][d+1]-grid[b+1][c]+grid[a][c]

v = 448

n,m,q = readints()
intervals = list()
for _ in range(n):
    l,r = readints()
    intervals.append((l,r))

#ar = list()

#for i in range(n//v):
#    ar.append(condense(m,intervals,i*v,i*v+v))

supergrid = create_supergrid(n,m,v,intervals)

for _ in range(q):
    a,b,c,d = readints()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    ai = a//v
    bi = b//v
    ans = 0
    if bi-1 > ai:
        ans += compute(supergrid,ai+1,bi-1,c,d)
        for e in range(a,ai*v+v):
            l,r = intervals[e][0]-1,intervals[e][1]-1
            mi,ma = max(l,c),min(r,d)
            ans += max(0,ma-mi+1)
            
        for f in range(bi*v,b+1):
            l,r = intervals[f][0]-1,intervals[f][1]-1
            mi,ma = max(l,c),min(r,d)
            ans += max(0,ma-mi+1)
    else:
        for e in range(a,b+1):
            l,r = intervals[e][0]-1,intervals[e][1]-1
            mi,ma = max(l,c),min(r,d)
            ans += max(0,ma-mi+1)
    print(ans)
