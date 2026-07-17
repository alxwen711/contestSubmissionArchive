import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
trade value must exceed k
greedy min/max check
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    ans = 0
    mi,ma = 999999999999999999,-9999999999999999999999
    for i in ar:
        mi = min(i,mi)
        ma = max(i,ma)
        if ma-mi > k:
            ans += 1
            mi,ma = 999999999999999999,-9999999999999999999999
    print(ans)        
