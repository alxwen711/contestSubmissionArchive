import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
trivial O(n^2) sol is to solve by running total from start,
then starting at index 1,2,3...n-1
"""
n = readint()
ar = readar()
