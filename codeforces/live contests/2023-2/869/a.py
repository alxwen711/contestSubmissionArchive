import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# must agree with self [0]
for i in range(readint()):
    n,k = readints()
    ans = 1
    s = input()
    for j in range(n-1):
        if input() == s: ans += 1
    print(ans)
