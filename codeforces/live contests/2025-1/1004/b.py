import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
any sequence without a 0 is magical
if 0 appears, it must be exactly once
something involving duplicates

last testcase 011

001122334455667788 is magical? (no)
876543210 is magical

locate last 0, create sequence comprising of all non-0's to the left x
321110


320111 is magical

one of the 0 values has to be chosen as a fixed pt
how to involve previous possible violations?
"""

def solve(n,ar):
    best = n
    for i in range(n):
        if ar[i] == 0:
            best -= 1
    if best == n: return best
    br = list()
    fixedpts = list()
    for a in range(n):
        if ar[a] != 0: br.append(ar[a])
        else: fixedpts.append(len(br))
    fixedpts = list(set(fixedpts))
    fixedpts.sort()
    # if br is mexable, then return br's len (best+1)
    mex = [0]*(n+3)
    for c in br:
        if c <= n: mex[c] += 1
    mex[0] = 1000000 # assume infinite mex count
    index = 0
    while mex[index] != 0:
        index += 1
    mi = 6986794693698439689693
    fixindex = 0
    for f in range(len(br)):
        if f == fixedpts[fixindex]: # check for passage
            if mi >= index: return best+1
            fixindex += 1
            if fixindex == len(fixedpts): return best
        mi = min(f,mi)
        if f <= n:
            mex[f] -= 1
            if mex[f] == 0 and f < index: index = f
    return best+1



for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
