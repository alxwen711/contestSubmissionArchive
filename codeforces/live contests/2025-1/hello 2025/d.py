import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
2 8 8 8 8 10 5 5 5 5 5 1
1 3 5 7 9
"""


for _ in range(readint()):
    n,q = readints()
    ar = readar()
    for _ in range(q):
        p,x = readints()
