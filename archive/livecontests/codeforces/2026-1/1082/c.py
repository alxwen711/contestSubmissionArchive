import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
12345322
once this starts decreasing, can only increment by 1
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    prev = 462387463874678364873264783624
    rv = 48762834687326487364
    ans = 0
    for i in ar:
        if i > rv or i <= prev:
            ans += 1
            prev = i
            rv = prev+1
        else:
            rv = i+1
    print(ans)
