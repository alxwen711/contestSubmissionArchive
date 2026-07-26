import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
4 4 4 4 case has 4/5 at the ends and 1/2/3 anywhere in the middle

 3 3 4 2
3 1 ? ? 2

 3 3 5 5 5
3 L H ? ? H
3 _ H _ _ H
L = 1/2
H = 5/6
2 ways for H
L has 2 choices
the two remaining can go either order

 2 3 2
2 _ _ 2??

rules:
this must be built as a mountain
highest value can only be n-1, which must exist
if neither endpoint is n-1, they cannot be equal
if an increasing value is found in the mountain:
then if this is n-1, log this as a high point and stop
otherwise, a fixed value MUST be present here
(if this means a value would appear twice, then impossible)

after all this is done, answer is to determine how
to fill in the remaining values so that the mountain is NOT altered
for this, count the holes in most restrictive conditions first

setup minimum and maximum values for each?

 1 3 5 4 2 
1 3 5 6 4 2


"""

facts = [1,1]
mod = 998244353
for i in range(2,1000005):
    facts.append((facts[-1]*i) % mod)

def solve(n,ar):
    if max(ar) == n: return 0.1
    if ar[0] == ar[-1]:
        # either this is the n-1 case or impossible
        if ar.count(n-1) == n-1:
            return (facts[n-2]*2) % mod
        return 0.2 # impossible
    br = list() # important value points
    cr = list()
    lb,rb = -1,-1
    if ar[0] == n-1:
        # check the whole thing is decreasing
        br.append((0,n-1))
        for j in range(n-2):
            if ar[j] < ar[j+1]: return 0.3
    else:
        # run increasing build, note lb
        br.append((0,ar[0]))
        for j in range(n-2):
            if ar[j] > ar[j+1]: return 0.4
            if ar[j] < ar[j+1]:
                if ar[j+1] == n-1:
                    br.append((j+1,n-1))
                    lb = j+1
                    break
                else: br.append((j+1,ar[j+1]))
        if br[-1][1] != n-1: return 0.5
    if ar[-1] == n-1:
        # check the whole thing is increasing
        cr.append((n-1,n-1))
        for j in range(n-2):
            if ar[j] > ar[j+1]: return 0.6
    else:
        # run increasing build, note rb
        cr.append((n-1,ar[-1]))
        for j in range(n-2,0,-1):
            if ar[j] > ar[j-1]: return 0.7
            if ar[j] < ar[j-1]:
                if ar[j-1] == n-1:
                    cr.append((j,n-1))
                    rb = j-1
                    break
                else: cr.append((j,ar[j-1]))
        if cr[-1][1] != n-1: return 0.8

    if lb != -1 and rb != -1: # check that everything in this range is n-1
        for j in range(lb,rb+1):
            if ar[j] != n-1: return 0.9
    #print(br,cr)
    # verify the boundary points are not duplicated and valid        
    h = [1]*(n+1)
    h[0] = 0
    h[n] = 0
    h[n-1] = 2
    for b in br:
        h[b[1]] -= 1
        if h[b[1]] == -1: return 0.91
    for c in cr:
        h[c[1]] -= 1
        if h[c[1]] == -1: return 0.92
    if h[n-1] != 0: return 0.93
    
    # compute the answer from the boundary points
    segments = list()
    for b in range(len(br)-1):
        if br[b][0]+1 < br[b+1][0]:
            segments.append((br[b][1],br[b+1][0]-br[b][0]-1)) # maximal allowed value, number of vals to fill
    for c in range(len(cr)-1):
        if cr[c+1][0]+1 < cr[c][0]:
            segments.append((cr[c][1],cr[c][0]-cr[c+1][0]-1)) # maximal allowed value, number of vals to fill
    ptr = 0
    left = 0
    segments.sort()
    #print(segments)
    ans = 2
    for s in segments:
        while ptr != s[0]:
            left += h[ptr]
            ptr += 1
        for _ in range(s[1]):
            if left == 0: return 0.94
            ans = (ans*left) % mod
            left -= 1
    while ptr != n:
        left += h[ptr]
        ptr += 1
    return (ans*facts[left]) % mod

        
for _ in range(readint()):
    n = readint()
    ar = readar()
    v = solve(n,ar)
    print(v if v >= 1 else 0)
