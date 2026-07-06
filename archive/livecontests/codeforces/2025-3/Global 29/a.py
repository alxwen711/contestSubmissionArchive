import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 1
2 1
3 3
5 1
5 4
are impossible
"""

for _ in range(readint()):
    x,y = readints()
    if x == y+1 or x == y or y == 1: print(-1)
    elif y > x: print(2)
    else: print(3)
