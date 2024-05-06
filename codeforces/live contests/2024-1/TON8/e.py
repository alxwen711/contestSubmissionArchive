import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
find the pattern question
2 1 -> 0
3 1 -> 2
4 1 -> 4
5 1 -> 8
6 1 -> 12
7 1 -> 18
8 1 -> 24
420 69 -> 870279412
"""

m = 998244353

for _ in range(readint()):
    l,n = readints()
