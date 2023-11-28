import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# number of trees is n**(n-2)
"""
n is up to 500 and 4 seconds,
maybe something O(n**3)?

first step is make n*n table for inversion detection
prufer code might be useful?
"""

n = readint()
ar = readar()
