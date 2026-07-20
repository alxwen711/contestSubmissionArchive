import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
By pigeonhole, k is at most m
"""

for _ in range(readint()):
    n,k,m = readints()
    if k > m: print("NO")
    else:
        ans = [1]*n
        ans[0] = m-k+1
        print("YES")
        print(*ans)
