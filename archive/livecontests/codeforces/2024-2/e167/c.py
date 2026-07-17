import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if a side is higher, use that side
only track 1/1 or -1/-1
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    a,b = 0,0
    one = 0
    minusone = 0
    for i in range(n):
        if ar[i] > br[i]: a += ar[i]
        elif ar[i] < br[i]: b += br[i]
        elif ar[i] == 1: one += 1
        elif ar[i] == -1: minusone += 1
    if minusone != 0:
        diff = abs(a-b)
        if a > b:
            a -= min(diff,minusone)
            minusone -= min(diff,minusone)
        elif b > a:
            b -= min(diff,minusone)
            minusone -= min(diff,minusone)
        # a and b are either equal and/or minusone == 0
        a -= minusone//2
        b -= ((minusone+1)//2)
    if one != 0:
        diff = abs(a-b)
        if a > b:
            b += min(diff,one)
            one -= min(diff,one)
        elif b > a:
            a += min(diff,one)
            one -= min(diff,one)
        # a and b are either equal and/or one == 0
        a += one//2
        b += ((one+1)//2)
    print(min(a,b))
