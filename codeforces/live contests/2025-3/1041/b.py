import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
only block that matters is the first block as close left/right
"""


for _ in range(readint()):
    n,x = readints()
    s = readin()
    if x == 1 or x == n: print(1)
    else:
        a = x-1
        b = x+1
        while a != 0:
            if s[a-1] == ".": a -= 1
            else: break
        while b != n+1:
            if s[b-1] == ".": b += 1
            else: break
        ad = a+1
        bd = n+2-b
        if ad < bd: ad = x
        else: bd = n-x+1
        print(min(ad,bd))
