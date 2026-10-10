import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
x and y are relatively small (0 to 500)
any z 500000+ should just move?
some sort of pruning?

suppose we had a fixed point where we spam magic the rest of the way
find the minimal cost assuming you MUST finish at x

is this A*? construct a greedy idea first? unsure if there is an
actually good metric to use for A* distance estimation
"""

for _ in range(readint()):
    n = readint()
    ar = list()
    br = list()
    cr = list()
    prefix = [0]
    for c in cr:
        prefix.append(prefix[-1]+c)
    for _ in range(n):
        x,y,z = readints()
        ar.append(x)
        br.append(y)
        cr.append(z)
    greed = 0
    a,b = 0,0
    for i in range(n):
        mvcost = abs(ar[i]-a)**2+abs(br[i]-b)**2
        if mvcost <= cr[i]:
            greed += mvcost
            a,b = ar[i],br[i]
        else:
            greed += cr[i]
    # naive greedy acts as the minimal cost for the A*
    

            
