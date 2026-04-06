import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 2 3
01
10
11

10 01
11 01
11 10
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    for i in ar:
        for j in ar:
            ans = max(ans,i^j)
    print(ans)
