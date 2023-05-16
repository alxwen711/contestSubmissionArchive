import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
inc amounts are 1,2,3,4,5...
if not required do not dec on blue
final minimum can be lower than base
[1,1,1,1,1], do 20 operations
not necessarily bin searchable
"""
n,q = readints()
ar = readar()
br = readar()
ans = list()
ar.sort()
for x in br:
    low = -1000000000
