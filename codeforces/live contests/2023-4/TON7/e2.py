import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
maybe brute force isn't that long?
"""
def solve(n,ar):
    ans = [-1]*n
    it = 0
    r = n
    miss = list()
    for i in range(n):
        miss.append(i)
    while r != 0:
        #find misplaced
        tmp = list()
        for j in miss:
            if ar[j] != j+1: tmp.append(j)
            else: ans[j] = it
        if len(tmp) == 0: break
        #det min shift
        miss = tmp
        r = len(miss)
        vals = list()
        for k in miss:
            vals.append(ar[k])
        d = {}
        for m in range(r):
            d[vals[m]] = m
        ms = 999999999999999999999999
        for p in range(r):
            target = d[miss[p]+1]
            ms = min(ms,(p-target) % r)

        #conduct ms
        it += ms
        for u in range(r):
            ar[miss[u]] = vals[(u-ms) % r]
        
        
    print(*ans)
        
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)


