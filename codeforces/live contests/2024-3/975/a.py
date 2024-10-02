import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
you cannot add any new numbers in
largest deck size possible is n, attempt trials?
a setup of x may not mean setup of x-1 is possible
"""

def f(n,ar,k):
    ar.sort()
    s = sum(ar)
    for x in range(n,1,-1):
        req = -s % x
        if k < req: continue
        # then determine that some iteration actually exists
        cards = (s+k)//x*x # total card count
        if ar[-1]*x <= cards: return x
    return 1
for _ in range(readint()):
    n,k = readints()
    ar = readar()

    print(f(n,ar,k))
