import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
(0,1),(1,2) differs from (1,2),(0,1)
how many operations are possible
so that all places that differ
are still in a single segment?

let 1 be pos that differs, 0 not
must after 1 op have only 1 group of 1's
if 3+ groups of 1 (11001100110), 0 solutions
2 groups (00111100011100)

cannot reach the solved case in 1 operation
"""

for i in range(readint()):
    n = readint()
    s = sys.stdin.readline()
    t = sys.stdin.readline()
    ar = list()
    seg = False
    st = -1
    for j in range(n):
        if seg: #in segment
            if s[j] == t[j]:
                seg = False
                ar.append((st,j-1))
        else: #not in segment
            if s[j] != t[j]:
                seg = True
                st = j
    if seg: ar.append((st,n-1))
    x = len(ar)
    if x == 0: #anything for first, then clone
        #1+2+3...+n
        print((n*n+n)//2)
    elif x == 1: #no segment split allowed, AND no making a new segment
        #how many ways to keep as 1 segment
        a,b = ar[0][0],n-ar[0][1]-1
        ans = (a+b)*2
        l = ar[0][1]-ar[0][0]
        ans += l*2
        """
        ans = (n*n+n)//2-1 #going directly to solved is not allowed
        #seg split
        l = max(0,ar[0][1]-ar[0][0]-1)
        ans -= (l*l+l)//2
        #l/r cases fail on 01110, swap last two to get 01101
        #l
        l = max(0,ar[0][0]-1)
        ans -= (l*l+l)//2
        #r
        l = max(0,n-ar[0][1]-2)
        ans -= (l*l+l)//2
        #l and r
        a,b = ar[0][0],n-ar[0][1]-1
        ans -= a*b
        """
        print(ans)
        
    elif x == 2: print(6) 
    else: print(0) #impossible
