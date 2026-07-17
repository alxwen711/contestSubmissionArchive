import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,k = readints()
    s = readin()
    if k > n//2: print(-1)
    else:
        ans = 0
        for i in range(k):
            if s[i] == "L": ans += 1
            if s[-i-1] == "R": ans += 1
        print(ans)
