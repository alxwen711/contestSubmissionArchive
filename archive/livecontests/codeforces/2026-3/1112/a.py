import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
rlrlrl sequence required
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n % 2 == 1: print("NO")
    else:
        a,b = ar[0],ar[1]
        for u in range(2,n,2):
            a = min(ar[u],a)
            b = max(ar[u+1],b)
        print("YES" if b+1 < a else "NO")
