import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the action must be done exactly n times
the values can be rearranged to make the array
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    ar.reverse()
    while ar[-1] == 0:
        ar.pop()
    s = sum(ar)
    # there must be at least a total of n-1 left
    print(min(s-(n-1),len(ar)))
