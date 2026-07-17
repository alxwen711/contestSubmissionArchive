import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# tree dp?
"""
probably some sort of O(n^2 log n) type solution
number of times the edge is involved in the tree?
works for sample 1? sample 2 is only 468 under this method
"""
