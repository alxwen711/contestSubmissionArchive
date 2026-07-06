import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
y vals may not be sequential, but x[i] < y[i] for 1 <= i <= n
removing different takeouts could have similar evil chains
ie. 1 takes 4, 4 takes 5, 5 takes 6
generate a bipartite graph where connections are with own takeout
and the next earliest?
emulate a normal setup to find alt take, record order of takeouts
"""

def solve(n,ar,br):
    events = list()
    for i in range(n):
        events.append([ar[i],i,1]) #arrival
        events.append([br[i],i,2]) #takeout
    events.sort()
    lowest = 999999999
    lowest2 = 999999999
    h = [0]*n
    for j in range(2*n):
        event = events[j]
        if event[2] == 1: #arrival
            # need to track lowest two elements in O(1) time
            # use indexed heap???
            # note: meaning of above is a heapq but with an
            # added dict tracking the indices of each element
            # wolud have the issue of not supporting dup elements
            h[event[1]] = 1
            #if event[1]
    # pair with same takeout and lowest index
    # try from earliest takeout (how to order nodes?)
    # those later in the chain should be suboptimal
    return -1

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))
