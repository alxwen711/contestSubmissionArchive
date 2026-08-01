import sys
from math import lcm,gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
does obtaining the first x rewards over and over exceed
a full cycle spam?

idea here is that for stop len a, there will be some sort of desync

feels like there is a possibility of a midpoint desync

length 4 -> 14+3*3
full length 6 -> 18+6*3
36*2 23*3

4-3 

not even base cycling actually works on samples

is this crt
(find minimal alignment between an arbritary cycle length and some
remainder point??)

so generalized steps for this are as follows:
under each intentional length for a smaller array (ar[i] boundaries):
length will be ar[i]+1
find distance d such that d % (ar[i]+1) = ar[i] (avoiding 0)
and d % n = ar[j]-1 for each j from 0 to m-1
this may not always exist; mainly if ar[i]+1 and n are not coprime
in this case, readjust ar[j]-1 to ar[j]-y, y being min value such that
everything can be divided and there is a solution (may need to check
there are no additional boosts being ejected from this process?)

After that then CRT is used to find d (somehow, implementation of this
in the remaining time is impossible)

after which then use a basic computation to find both sums
repeat until a valid answer is found, else NO

compute + bsearch is fine
samples are optimized; i = 1 x = 7 is necessary

editor note: E is apparently not CRT from asking in solved.ac server?
then I really have no clue what this is, surely the n <= 2000 implies
some sort of O(n^2)?

post solve stats show E probably being around 1800 rating, so it's very
likely something less crazy than CRT can be used
"""

def bsearch(ar,prefix,x):
    low = 0
    high = len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if x >= ar[mid]: low = mid
        else: high = mid
    if x >= ar[high]: return prefix[high+1]
    elif x >= ar[low]: return prefix[low+1]
    else: return prefix[low]
    

def compute(ar,br,d,prefix,i,x):
    """
    given a specific L and x, determine if the L alternate is better
    i should be the index for boosting
    """
    
    length = ar[i]+1
    boost = prefix[i+1]
    # compute alternate score
    ac,r = x//length,x%length
    altscore = ac*((length-1)*d+boost)
    if r != 0:
        altscore += r*d
        altscore += bsearch(ar,prefix,r)

    # compute main score
    mc,mr = x//n,x%n
    mainscore = mc*(n*d+prefix[-1])
    if mr != 0:
        mainscore += mr*d
        mainscore += bsearch(ar,prefix,mr)
    print(i,x,altscore,mainscore)
    return altscore > mainscore
    
for _ in range(readint()):
    n,m,d = readints()
    ar = list()
    br = list()
    for _ in range(m):
        p,r = readints()
        ar.append(p)
        br.append(r)

    prefix = [0]
    for b in br:
        prefix.append(prefix[-1]+b)
    

    ans = "NO"
    baselen = n
    baseboost = sum(br)
    
    # run checks here
    length = 0
    boost = 0
    for i in range(m):
        length = ar[i]+1
        boost += br[i]
        if length >= n: break # no chance
        # naive cycle alignment, TODO: replace this with some sort of CRT
        g = gcd(length,n) # if this is not 1, then fulldist gets weird
        for j in range(m):
            """
            fulldist should be smallest value such that
            fulldist % length == length-1
            fulldist % n == ar[j]-1
            """
            fulldist = lcm(length,baselen)-1
            if compute(ar,br,d,prefix,i,fulldist):
                ans = "YES"
            break
    print(ans)
