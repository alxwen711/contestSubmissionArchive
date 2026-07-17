import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    s = readin()
    ans = 1
    if s[0] == "R":
        for i in range(1,n):
            ans += 1
            if s[i] == "L": break
    else:
        for i in range(n-1,0,-1):
            ans += 1
            if s[i] == "R": break
    print(ans)
