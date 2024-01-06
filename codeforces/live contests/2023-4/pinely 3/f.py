import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
track number of wrong values in range first (i-ar[i])
if 0, must be permutation

0 0 1 1 1 2 3 4 5 6 7 9 11 13 15
9 implies 13/14/15 in first 12 values
7 implies 12/13/14/15 in first 11 values
0 0 means 1/2 are in last 13 values
"""
