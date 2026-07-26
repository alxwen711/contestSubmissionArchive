import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
example 4 valid indices are 0,1,2

some sort of ds is needed?

might skip as I really have no clue how to begin this
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
