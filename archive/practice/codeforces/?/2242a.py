import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there must be either
3 of the same chr
2 pairs of chrs
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    ans = "NO"
    if ar[-1] >= 3: ans = "YES"
    elif n >= 2 and ar[-2] >= 2: ans = "YES"
    print(ans)
