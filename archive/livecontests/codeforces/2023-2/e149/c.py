import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
have as few 1/0 chains as possible?
"""
for i in range(readint()):
    s = sys.stdin.readline()[:-1]
    n = len(s)
    ans = [0]*n
    c = 0
    for j in range(n):
        if s[j] == "0":
            ans[j] = 0
            c = 0
        elif s[j] == "1":
            ans[j] = 1
            c = 1
        else:
            ans[j] = c
    print(*ans,sep="")
