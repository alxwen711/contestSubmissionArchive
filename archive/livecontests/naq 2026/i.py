import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
any i > j contradiction makes this impossible
must it just be exact condition must show? try that first
"""

for _ in range(readint()):
    n,m = readints()
    h = [1]*(n-1)
    flag = True
    for _ in range(m):
        a,b = readints()
        if a > b: flag = False
        if a+1 == b: h[a-1] = 0
    if not flag: print(-1)
    else: print(sum(h))
