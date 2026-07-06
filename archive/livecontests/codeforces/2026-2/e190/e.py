import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if under tolerance, 0
if at least tolerance, min(tolerance+distance,item)

find least irritating item for each user (query system)

2d seg tree???, search 8 specific zones???

p + c cannot be optimized for minimum here

store sums as additional value in nodes then binary search the
searching process, this just feels so inherently clunky
"""


n = readint()
pr = readar()
cr = readar()
m = readint()
tp = readar()
tc = readar()
d = readar()
