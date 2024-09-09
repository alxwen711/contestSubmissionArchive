import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
at a specific time, so lazy seg tree is forced if it is used
everyone does go in and out, can track when each person was in
how many segments can anyone really have?
100000 segments at most, each comparison can be done in linear time
worst case: 50k segment + 50k 1 segments
if size diff > 100, alternate binary search is better
"""

def speedsolve(ar,br,ref):
    a = len(ar)
    ans = 0
    for b in br:
        # smallest index larger than left val
        low = 0
        high = a-1
        while high-low > 1:
            mid = (low+high)//2
            if ar[mid][0] > b[0]: high = mid
            else: low = mid
        li = -1
        if ar[low][0] > b[0]: li = low
        elif ar[high][0] > b[0]: li = high
        else: li = high+1

        # largest index smaller than right val
        low = 0
        high = a-1
        while high-low > 1:
            mid = (low+high)//2
            if ar[mid][1] < b[1]: low = mid
            else: high = mid
        ri = -1
        if ar[high][1] < b[1]: ri = high
        elif ar[high][1] < b[1]: ri = low
        else: ri = low-1
        if ri != -1 and li != a:
            # fully enclosed sections
            if li <= ri:
                ans += ref[ri+1]-ref[li]
            if li-1 == ri: ans += b[1]-b[0]
            else:
                if li != 0:
                    if ar[li-1][1] > b[0]: ans += ar[li-1][1]-b[0]
                if ri != a-1:
                    if b[1] > ar[ri+1][0]: ans += ar[ri+1][0]-b[1]
    return ans
        
def prefix(ar):
    br = [0]
    for i in ar:
        br.append(i[1]-i[0]+br[-1])
    return br

def solve(ar,br):
    a,b = len(ar),len(br)
    if a*20 <= b: return -1
    if b*20 <= a: return -2
    # standard line procedure method
    cr = list()
    for aa in ar:
        cr.append((aa[0],0))
        cr.append((aa[1],0))
    for bb in br:
        cr.append((bb[0],1))
        cr.append((bb[1],1))
    cr.sort()
    prev = 0
    ai,bi = 0,0
    ans = 0
    for c in cr:
        if ai == 1 and bi == 1: ans += c[0]-prev
        if c[1] == 0: ai ^= 1
        else: bi ^= 1
        prev = c[0]
    return ans

n,m = readints()
office = [0]*(n+1)
times = list()
for _ in range(n+1):
    tmp = list()
    times.append(tmp)
for _ in range(m):
    t,p = readints()
    if office[p] == 0: office[p] = t
    else:
        times[p].append((office[p],t))
        office[p] = 0
ref = list()
tmp = list()
ref.append(tmp)
for i in range(1,n+1):
    ref.append(prefix(times[i]))

d = {}
for _ in range(readint()):
    a,b = readints()
    if d.get((a,b)) == None:
        d[(a,b)] = solve(times[a],times[b])
        if d[(a,b)] == -1: d[(a,b)] = speedsolve(times[b],times[a],ref[b])
        elif d[(a,b)] == -2: d[(a,b)] = speedsolve(times[a],times[b],ref[a])
        
    print(d[(a,b)]) # no dup calcs
