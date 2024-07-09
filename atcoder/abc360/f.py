import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
lowest l/r combo should occur at the start of sectionsish
l is some section start +1
r is some section start +1
O(n^2 log n) is possible from observation, reduce to O(n log n)
"""

n = readint()
ar = list()
for _ in range(n):
    a,b = readints()
    if a+1 != b: ar.append((a,b)) # else impossible
