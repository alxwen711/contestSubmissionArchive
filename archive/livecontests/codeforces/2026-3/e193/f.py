import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is at most 500000, array values up to 10^9, 5 seconds

1 to n set, 4 beauty values that are possible:

0 -> 4 9 14 19
1 -> 2 3 4 5, 3 4 5 6
2 -> ?
3 -> ?
4 -> 1 2 3 4
5 -> ?
6 -> ?

then this seems to be equivalent to ensuring x,2x,3x,4x never appear in the set

dp up to n/4
the later values have less collision?
"""

n = readint()
ar = readar()
