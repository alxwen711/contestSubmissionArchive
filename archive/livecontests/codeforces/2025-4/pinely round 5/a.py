import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    r,x,d,n = readints()
    ans = 0
    s = readin()
    for i in s:
        if i == "1":
            ans += 1
            r -= d
        elif r < x:
            ans += 1
            r -= d
    print(ans)
