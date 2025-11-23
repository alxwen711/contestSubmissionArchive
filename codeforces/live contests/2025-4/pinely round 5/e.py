import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# probably dp
"""
k >= 3 (no k = 1 trivial case)

starting from the back, count the base number of ways to get certain +- vals
after k-1, first requirement is obtained
if 0/1, remove all negative/positive scores
how to do substring subtractions???
"""

m = 998244353

for _ in range(readint()):
    n,k = readints()
    s = readin()
    s.reverse() # last chr of substring determines the majority

