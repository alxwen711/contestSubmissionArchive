import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]

"""
consecutive P/S -> already determined value
P at start -> first value forced
P at end -> total sum of values forced
S at start -> total sum of values forced
S at end -> last value forced

n can ONLY be at most 2000
"""

for _ in range(readint()):
    n,m = readints()
    s = readin()
    ar = readar()
