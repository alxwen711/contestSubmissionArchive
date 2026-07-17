import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
fix all B's to A's first is possible
if then any more errors, must check if C's are there

AA  
BA BB 
      CC
CBBBB
BBBBA

ABBBBBB -> BBBBBBA

anywhere Y has a C, X must have one as well
in between C sections, X and Y must have
same number of A/B
if X has C's, can be translated to A/B as needed
X has to have further left A's than Y
"""

def test(ar,br,aa,ab,ba,bb,st,ed):
    if st > ed: return True
    if aa > ba or ab > bb: return False
    acount = 0
    bcount = 0
    for x in range(st,ed+1):
        #ar
        if ar[x] == "A": acount += 1
        elif ar[x] == "C" and aa < ba:
            aa += 1
            acount += 1
        #br
        if br[x] == "A": bcount += 1

        if bcount > acount: return False
    return True
    
def solve(n,ar,br):
    t = 0
    aa,ab,ba,bb = 0,0,0,0
    for i in range(n):
        if br[i] == "C":
            if ar[i] != "C": return "No"
            if not test(ar,br,aa,ab,ba,bb,t,i-1): return "No"
            aa,ab,ba,bb = 0,0,0,0
            t = i+1
        if ar[i] == "A": aa += 1
        elif ar[i] == "B": ab += 1
        if br[i] == "A": ba += 1
        elif br[i] == "B": bb += 1
    if t != n:
        if not test(ar,br,aa,ab,ba,bb,t,n-1): return "No"
    return "Yes"

for oneoten in range(readint()):
    n,x,y = map(str,sys.stdin.readline().split())
    n = int(n)
    ar = list()
    br = list()
    for i in range(n):
        ar.append(x[i])
        br.append(y[i])
    print(solve(n,ar,br))
    
