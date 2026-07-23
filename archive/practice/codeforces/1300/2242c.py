import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of unique elements after a deletion -> spam if modulo hits
"""


for _ in range(readint()):
    n,k = readints()
    ar = readar()
    prev = ar[0]
    c = 0
    h = [0]*(n+1)
    for i in ar:
        if i == prev:
            c += 1
        else:
            h[c] += 1
            c = 1
            prev = i
    h[c] += 1
    s = sum(h) # number of unique elements
    minsetsize = n
    ans = 0
    for a in range(1,n+1):
        if h[a] != 0: # breaking point for a minsetsize
            if k >= minsetsize and (k-minsetsize) % s == 0: ans += 1
        minsetsize -= s
        s -= h[a]
        if s == 0: break
    print(ans)
