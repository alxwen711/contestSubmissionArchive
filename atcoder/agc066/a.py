import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
min changes to array
maximum total change allowed is d*n*n/2 (avg d/2 per cell)
cost is abs value, can decrement values
"""

n,d = readints()
ar = list()
for _ in range(n):
    tmp = readar()
    ar.append(tmp)
