import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
4 3

"""


for _ in range(readint()):
    n = readint()
    ans = []
    for i in range(2*n,n,-1):
        ans.append(i)
    print(*ans)
