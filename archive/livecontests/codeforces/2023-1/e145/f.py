import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
fuel buying strat:
if 1, buy until capped or have enough to complete
else wait as long as possible, then buy enough 2 to get to next stop
any 1 spot will have min cost
track cost of 1 loop
for 2 spots track where next 1 is
2 cost -> dist to 1 * 2 + cost of remaining loop

what needs to be tracked:
distance between any two cities (sum array)
cost between any two cities on 1 path (sum array + 2-segmenting)
"""

def calcmc(n,k,ar,br,x):
    loc = x
    fuel = k
    ans = [0]*n
    cost = 0
    for i in range(n):
        dist = ar[loc]
        fuel -= dist
        cost += dist
        if fuel < 0:
            cost += -fuel
            fuel = 0
        loc = (loc+1) % n
        ans[loc] = cost
        if br[loc] == 1: fuel = k
    return ans,ans[loc]

def solve(n,k,ar,br):
    first = -1
    dist = [0]*(n+1) #dist of first (i+1) cities
    for i in range(n):
        dist[i+1] = dist[i]+ar[i]
        if first == -1 and br[i] == 1: first = i
    if first == -1: #everything is 2
        ans = [dist[-1]*2]*n
        print(*ans)
        return
    #calc min cost
    costs,mc = calcmc(n,k,ar,br,first)
    h = [-1]*n
    prev = -1
    for snth in range(n):
        if br[n-snth-1] == 1: prev = n-snth-1
        else: h[n-snth-1] = prev
    twoep = n-1
    while br[twoep] == 2:
        h[twoep] = prev
        twoep -= 1
    ans = list()
    for m in range(n):
        if h[m] == -1: ans.append(mc) #1 gas station
        else:
            c = dist[h[m]]-dist[m]
            if h[m] == 0:
                c = dist[-1]-dist[m]
            elif h[m] < m:
                c = dist[-1]-dist[m]+dist[h[m]]
            c *= 2
            # distance from h[m] to m
            if h[m] == first:
                c += costs[m]
            else:# h[m] <> m
                cc = costs[m]-costs[h[m]]
                if cc < 0: cc += mc
                c += cc
            ans.append(c)
    #print(mc)
    #print(costs)
    #print(h)
    print(*ans)

                
for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar() # only has 1 and 2
    solve(n,k,ar,br)
