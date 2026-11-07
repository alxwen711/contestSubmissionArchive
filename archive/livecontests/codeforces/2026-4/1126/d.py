import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
boundary moves; find segements where s moves such that:
infected += 1 or infected -= 1

m people

the outputted s is forced to be in range 1 to 10**18

events
2,1
7,-1
7,-1
12,1
"""

for _ in range(readint()):
    n,m,k = readints()
    segments = list()
    for _ in range(n):
        l,r = readints()
        segments.append((l,r))
    events = list()
    for s in segments:
        l,r = s[0],s[1]
        events.append((l-m,1)) # right enters in next
        events.append((r-m+1,-1)) # right exits out
        events.append((l,-1)) # left starts removing
        events.append((r+1,1)) # left stops removing
    events.sort()
    index = events[0][0]
    s = 0
    inc = 0
    ans = -1
    for e in range(len(events)-1):
        inc += events[e][1]
        dist = events[e+1][0]-events[e][0]
        if inc == 1:
            if s+dist >= k and s <= k:
                pans = index+k-s
                if pans > 0:
                    ans = pans
                    break
        elif inc == -1:
            if s-dist <= k and s >= k:
                pans = index+s-k
                if pans > 0:
                    ans = pans
                    break
        else:
            if s == k:
                pans = events[e+1][0]
                if pans > 0:
                    ans = pans
                    break
        s += inc*dist
        index = events[e+1][0]
        #print(s,index)
    #print(events)
    print(ans)
