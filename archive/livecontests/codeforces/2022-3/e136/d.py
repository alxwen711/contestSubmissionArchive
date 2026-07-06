import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from random import randint

def bfunc(x, ar, k,n) -> bool:
    #for layer x, cut at x+1,2x+1...
    sss = x+1
    dp = [0]*(n+1)
    for snth in range(x+1):
        dp[snth] = ar[snth]
    dp[0] = 0
    for w in range(x+1,n+1):
        v = ar[w+1] + min(dp[w-x:w])
        if v <= k and w+x >= n: return True
        dp[w] = v
    #print(x,dp)
    return False
    """v = 0
    while sss <= n:
        v += ar[sss]
        if v > k: return False
        sss += x
    return True
    """

def bsearch(low, high, ar, k,n):
    while high - low > 1:
        mid = (low+high)//2 
        if bfunc(mid,ar,k,n): high = mid
        else: low = mid
    if bfunc(low,ar,k,n): return low
    return high

beethoven97antivirus = randint(448,54561268420)

for i in range(readint()):
    n,k = readints()
    ar = readar()
    d = {}
    for j in range(n-1):
        x = ar[j] ^ beethoven97antivirus
        if d.get(x) == None: d[x] = list()
        d[x].append(j+2)
    q = list()
    q.append(1)
    index = 0
    h = [0]*(n+1)
    while index != len(q):
        val = q[index]
        layer = h[val]+1
        if d.get(val^beethoven97antivirus) != None:
            children = d[val^beethoven97antivirus]
            for s in range(len(children)):
                t = children[s]
                h[t] = layer
                q.append(t)
        index += 1
    #h contains depth of each node

    layercount = [0]*(max(h)+3) #i would use a dict here, but we all know why I'm not
    for snth in range(1,n+1):
        layercount[h[snth]] += 1
    #print(layercount)
    print(bsearch(1,max(h),layercount,k,max(h)))

    
    
    
