import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
only need to find the highest value
binary idea could work (total cost about 2n^2)
note: cannot test EVERY pair of indicies
also cannot do sparse table, with 2000, second step
is 1000ish 1000 arrays
use small arrays to eliminate possible spots?
"""
