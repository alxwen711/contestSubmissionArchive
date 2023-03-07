import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
choose each k greedily?
runs through array once for each k selection for something like O(20n log n)
something with bridging a gap of negative vals between positive islands
"""
for i in range(readint()):
    n,k,x = readints() # k is at most 20
    ar = readar()
    for j in range(n):
        ar[j] -= x
    if x == 0 or k == 0 or k == n: #just find maxsum
        if k == n:
            for nn in range(n):
                ar[nn] += 2*x
        br = [0]*n
        br[0] = ar[0]
        for s in range(1,n):
            br[s] = max(br[s-1],0)+ar[s]
        ans = max(br)
        if ans < 0: print(0)
        else: print(ans)
    elif x > 0: #normal case
        br = [0]*(n-k+1)
        br[0] = sum(ar[:k])
        for a in range(1,n-k+1):
            br[a] = br[a-1]+ar[a+k-1]-ar[a-1]
        cr = [0]*(n-k+1)
        cr[0] = br[0]
        for b in range(1,n-k+1):
            cr[b] = max(0,cr[b-1]-br[b-1]+ar[b-1])+br[b]
        #print(ar)
        #print(br)
        #print(cr)
        ans = max(cr)+2*k*x
        if ans < 0: print(0)
        else: print(ans)
    else: #alt case
        for rev in range(n):
            ar[rev] += 2*x
        x = -x
        k = n-k
        br = [0]*(n-k+1)
        br[0] = sum(ar[:k])
        for a in range(1,n-k+1):
            br[a] = br[a-1]+ar[a+k-1]-ar[a-1]
        cr = [0]*(n-k+1)
        cr[0] = br[0]
        for b in range(1,n-k+1):
            cr[b] = max(0,cr[b-1]-br[b-1]+ar[b-1])+br[b]
        #print(ar)
        #print(br)
        #print(cr)
        ans = max(cr)+2*k*x
        if ans < 0: print(0)
        else: print(ans)
