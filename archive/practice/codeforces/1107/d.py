import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
first value will be fixed in two states
use subarray +1 -1 +1 -1 ...
always optimal to keep as many possible chain outs as possible
now consider multiple increments/decrements
"""


for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    a,b = 0,0 # +1,-1
    ans = "YES"
    for i in range(n):
        diff = br[i]-ar[i]
        current = a-b
        if diff > current:
            # add a to make this work
            a += (diff-current)
        elif current > diff:
            # remove a if possible
            a -= (current-diff)
            if a < 0:
                ans = "NO"
                break
        a,b = b,a
    print(ans)
