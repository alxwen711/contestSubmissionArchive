import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

m = 998244353
"""
testcase 3, group into 12,3,45 indices for swapping
always put the lower values in ar?

112
234
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    ans = 2
    for i in range(n):
        if ar[i] > br[i]: ar[i],br[i] = br[i],ar[i]
    for j in range(n-1):
        if br[j] <= ar[j+1]:
            ans = (ans*2) % m
    print(ans)
