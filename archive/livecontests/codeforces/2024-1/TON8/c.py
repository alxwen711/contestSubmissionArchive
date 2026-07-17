import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
optimal triangle count is n-2
ideally choose points optimally that are usable
(square with pts 1 and 2 chosen cannot make anything)
gap 1: -0
gap 2: -2
gap 3: -3
create as many 1 gaps as possible,
priority is 3,2,5,4,7,6...
maybe just prioritize odd vals each time/subtract 2 as much as possible
priority 3,5,7,9...,1111111,even
"""

for _ in range(readint()):
    n,x,y = readints()
    ar = readar()
    ar.sort()
    br = list()
    for i in range(x-1):
        a,b = ar[i],ar[i+1]
        l = b-a-1
        br.append((-(l % 2),l//2,-l))
    a,b = ar[-1],n+1
    last = n-ar[-1]+ar[0]-1
    br.append((-(last % 2),last//2,-last))
    #print(ar)
    #print(br)
    br.sort()
    ans = n-2 # subtract from optimal
    for j in range(x):
        if y >= br[j][1]: y -= br[j][1] #either 0 or rm
        elif y == 0 and br[j][2] != -1: ans += br[j][2] # no further removal
        else: # partial removal
            l = -br[j][2]
            l -= (2*y)
            ans -= l
            y = 0
    print(ans)
