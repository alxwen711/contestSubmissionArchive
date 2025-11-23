import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
There must be some point at which the pattern collapses

find the first k values for the pattern

find the last k values for the pattern

if n % k != 0, this has to implode? (no)

12341234123


not entirely binary search because some values can be valid/invalid

could be binary if segments length k were tested, but this uses too many queries
"""
