import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
only up to 9 object types, 200 objects maximum
only up to 5 stages, ie. can only shuffle 4 times
"""

def log(ar):
    h = [0]*10
    for i in ar:
        h[i] += 1
    return h

def solve():
    # first stage
    n = readint()
    ar = readar()
    br = log(ar)
    
    # first determine what type the mimic is
    print("- 0",flush=True)
    cr = readar()
    dr = log(cr)
    if br == dr: #redo step
        print("- 0",flush=True)
        cr = readar()
        dr = log(cr)
    v = -1
    for snth in range(10):
        if dr[snth] > br[snth]:
            v = snth
            break
    nq = list()
    nq.append("-")
    nq.append(0)
    for ii in range(n):
        if cr[ii] != v: nq.append(ii+1)
    nq[1] = len(nq)-2
    print(*nq)
    flush()
    # then shuffle until there is a single odd one out
    cr = readar()
    if cr.count(v) == len(cr): #reshuffle
        print("- 0",flush=True)
        cr = readar()
    for d in range(len(cr)):
        if cr[d] != v:
            ans = "! "+str(d+1)
            print(ans,flush=True)
            return

for i in range(readint()):
    solve()
