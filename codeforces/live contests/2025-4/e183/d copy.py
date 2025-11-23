import sys
from itertools import permutations
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
inv value is the number of subsegments containing inversions
must be in range n-1 to n(n-1)/2+1-n, unless it's 2 or 3, those cases
are brute force

okay so rng probably does not work, try greedy idea?
"""
def invcount(n,ar):
    ans = 0
    for a in range(n-1):
        for b in range(a+1,n):
            if ar[b-1] > ar[b]:
                ans += n-b
                break
            #if f(ar[a:b+1]):
            #    ans += 1
    return ans

def onecycle(n,k):
    for a in range(n-1):
        for b in range(a+1,n):
            ar[a],ar[b] = ar[b],ar[a]
            if invcount(n,ar) == k:
                print(*ar)
                return True
            ar[a],ar[b] = ar[b],ar[a]
    ar.reverse()
    for a in range(n-1):
        for b in range(a+1,n):
            ar[a],ar[b] = ar[b],ar[a]
            if invcount(n,ar) == k:
                print(*ar)
                return True
            ar[a],ar[b] = ar[b],ar[a]
    return False

"""
for n in range(1,6):
    #n,t = readints()
    ar = [i for i in range(1,n+1)]
    for p in permutations(ar):
        print(p,invcount(n,p))
"""

def solve(n,k):
    #print(n,k)
    if k == 0:
        return [i for i in range(1,n+1)]
    if k == (n*n-n)//2:
        return [i for i in range(n,0,-1)]
    ar = list()
    k = (n*n-n)//2-k
    while k != 0:
        x = 2
        while (x*x+x)//2 <= k:
            x += 1
        ar.append(x)
        k -= (x*x-x)//2
    #print(ar)
    s = sum(ar)
    while s > n:
        x = ar.pop()
        s -= x
        k += (x*x-x)//2
    if len(ar) == 0: return -1    
    ans = [i for i in range(1,n+1)]
    ptr = 0
    for a in ar:
        # reverse ptr to ptr+a
        for b in range(a//2):
            ans[ptr+b],ans[ptr+a-b-1] = ans[ptr+a-b-1],ans[ptr+b]
        ptr += a
    ans.reverse()
    if k != 0:
        if ar[0] > 2:
            br = solve(ar[0],(ar[0]*ar[0]-ar[0])//2-k)
            if br == -1: return -1
            else:
                for j in range(n-k,n):
                    ans[j] = br[j-n+k]
        else: return -1
    return ans

for _ in range(readint()):
    n,k = readints()
    ar = solve(n,k)
    if ar == -1: print(0)
    else: print(*ar)
