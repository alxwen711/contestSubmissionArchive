import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
[] -> 1 if true, 0 otherwise
use some sort of seg tree to count inversions in each prefix
if an inversion total is given, a range of values must be given

p s p s type patterns are unclear
1 0 5 2

1 3 5 2
1 7 5 6

from a number of inversions on prefix, how to determine permutation?
-> ordered set type question

if it is higher than all previous or lower than all previous, then there is some
weird question here

other idea is to fill in all of the known values first then something
(backtracking feels like a TLE)
"""
