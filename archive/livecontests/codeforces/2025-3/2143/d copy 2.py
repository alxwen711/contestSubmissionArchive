import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of sequences that have at most one decrement?

1 2 3 4 5 3 2 is impossible
1 3 1 3 1 3 is possible (RBRBRB)
track the highest value that is R (colour as many as possible R)
1 3 1 5 1 7 1 6 <- this is possible (RBRBRBRR)
on first decrease, track the maximum recorded from 0 case and cur val as min
then all other values need to diverge out from this

4 2 1 is impossible
4 2 5

what are impossible sequences?

5 4 6 3 7 2 8 1 is possible? no

anything with a run of 3 decreasing should never be possible

use some sort of check

alternately, determine the number of ways to subsequence into 2 runs

segtree base is dict with freq counts

idea here is to do a seg tree setup
find number of increasing subsequences at each max value
merging bit is kinda screwy (ran out of time)
then once this is done, take sum of all sequences and add to 2 run cases
only problem is that 2 run case could still be a sequence, never really
determined what to do around this
also made a tactical error in thinking C was harder
C just assume max is possible

looking at it did i just overcomplicate my dp wack crap earlier?????

can the array be split into 2 nondecreasing subsequences?

do we combine nodes efficiently?

cannot be tracking two vals in decreasing since both have O(n) options;
actual algorithm has to be O(n^2) somehow
"""

m = 1000000007

def merge(ld,rd):
    d = {}
    ar = list(ld.keys())
    br = list(rd.keys())
    for i in br:
        d[i] = rd[i]
    for j in ar:
        if d.get(j) == None: d[j] = ld[j]
        else: d[j] = (ld[j]+d[j]) % m
    # weird combining wack crap
    ar.sort()
    br.sort()
    basev = max(ar[0],br[0])
    basea = ld[ar[0]]
    baseb = rd[br[0]]
    basetotal = (basea*baseb) % m
    pta,ptb = 1,1
    if br[0] >= basev:
        if d.get(basev) == None: d[basev] = basetotal
        else: d[basev] = (d[basev]+basetotal) % m
    while pta != len(ar) or ptb != len(br):
        if pta == len(ar): # increment b
            basev = max(basev,br[ptb])
            basetotal = (basetotal+basea*rd[br[ptb]])
            if br[ptb] >= basev:
                if d.get(basev) == None: d[basev] = basetotal
                else: d[basev] = (d[basev]+basetotal) % m
            baseb = (baseb+rd[br[ptb]]) % m
            ptb += 1
        elif ptb == len(br): # increment a
            basev = max(basev,ar[pta])
            basetotal = (basetotal+baseb*ld[ar[pta]])
            if br[-1] >= basev:
                if d.get(basev) == None: d[basev] = basetotal
                else: d[basev] = (d[basev]+basetotal) % m
            basea = (basea+ld[ar[pta]]) % m
            pta += 1
        elif br[ptb] < ar[pta]: # increment b
            basev = max(basev,br[ptb])
            basetotal = (basetotal+basea*rd[br[ptb]])
            if br[ptb] >= basev:
                if d.get(basev) == None: d[basev] = basetotal
                else: d[basev] = (d[basev]+basetotal) % m
            baseb = (baseb+rd[br[ptb]]) % m
            ptb += 1
        else: # increment a
            basev = max(basev,ar[pta])
            basetotal = (basetotal+baseb*ld[ar[pta]])
            if br[ptb-1] >= basev:
                if d.get(basev) == None: d[basev] = basetotal
                else: d[basev] = (d[basev]+basetotal) % m
            basea = (basea+ld[ar[pta]]) % m
            pta += 1
    return d

    
def create_seg(n,ar):
    seg = list()
    base = list()
    for i in ar:
        tmp = {}
        tmp[i] = 1
        base.append(tmp)
    seg.append(base)
    while len(seg[-1]) != 1:
        ns = list()
        for i in range(len(seg[-1])//2):
            ns.append(merge(seg[-1][2*i],seg[-1][2*i+1]))
        seg.append(ns)
    return seg

def query(seg,il,ir):
    d = None
    l,r = il,ir
    for i in range(len(seg)):
        if l > r: break
        if l % 2 == 1:
            if d == None:
                d = seg[i][l]
            else:
                d = merge(seg[i][l],d)
            l += 1
        if r % 2 == 0:
            if d == None:
                d = seg[i][r]
            else:
                d = merge(seg[i][r],d)
            r -= 1
        
        l //= 2
        r //= 2
    ans = 0
    for ii in d.keys():
        ans = (ans+d[ii]) % m
    return ans
for _ in range(readint()):
    n = readint()
    ar = readar()
    s = create_seg(n,ar)
    why = list()
    for i in range(n):
        why.append(query(s,0,i))
    #print(why)
    #print(query(s,0,n-1))
    ans = sum(why)
    print(ans)
    """
    d = {}
    d[(-1,-1)] = 1

    for a in ar:
        nd = {}
        for i in d.keys():
            v = d[i]
            if nd.get(i) == None: nd[i] = 0
            nd[i] = (nd[i] + v) % m
            if i == (-1,-1): # empty case
                if nd.get((-1,a)) == None: nd[(-1,a)] = 0
                nd[(-1,a)] = (nd[(-1,a)]+v) % m
            elif i[0] == -1: # no decreasing aspect yet
                if a < i[1]: # decreasing
                    if nd.get((i[1],a)) == None: nd[(i[1],a)] = 0
                    nd[(i[1],a)] = (nd[(i[1],a)]+v) % m
                else: # same or higher
                    if nd.get((-1,a)) == None: nd[(-1,a)] = 0
                    nd[(-1,a)] = (nd[(-1,a)] + v) % m
            else: # must be lower or something along that line
                if a >= i[0]: # move 1st in seq up
                    if nd.get((a,i[1])) == None: nd[(a,i[1])] = 0
                    nd[(a,i[1])] = (nd[(a,i[1])]+v) % m
                elif a >= i[1]: # move 2nd in seq up
                    if nd.get((i[0],a)) == None: nd[(i[0],a)] = 0
                    nd[(i[0],a)] = (nd[(i[0],a)] + v) % m
        d = nd
    ans = 0
    for snth in d.keys():
        ans = (ans+d[snth]) % m
    print(ans)
    """


        
