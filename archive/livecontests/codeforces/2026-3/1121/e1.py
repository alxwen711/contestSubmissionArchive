import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy version is O(n^2 log n)
hard version is O(n log n)

2,4,8,16...
3,9,27,81...
5,25,125,625...

these sort of chains have problems (can be dropped to min-1)
every other subsequence should be able to just go to minimum?

15,25,125 would be set to 14 (14,24,124 seems possible)
"""

m = 998244353

for _ in range(readint()):
    n = readint()
    ar = readar()
