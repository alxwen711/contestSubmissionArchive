import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
FBFFBFFB FBFFBFFB
"""
x = "FBFFBFFBFBFFBFFBFBFFBFFB"
for i in range(readint()):
    n = readint()
    s = input()
    ans = "NO"
    for j in range(25-n):
        if x[j:j+n] == s:
            ans = "YES"
            break
    print(ans)
