import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
every 3 consecutive satisfy mex = max-min
all must be the same and not 0?
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = "YES"
    br = list()
    for i in range(n):
        if ar[i] != -1: br.append(ar[i])
        if ar[i] == 0: ans = "NO"
    for k in range(len(br)-1):
        if br[k] != br[k+1]: ans = "NO"
    print(ans)
