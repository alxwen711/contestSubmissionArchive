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
    prev = " "
    ans = 0
    for i in s:
        if i != prev: ans += 1
        prev = i
    if ans != n and ans != 1 and s[0] != s[-1]: ans += 1
    print(ans)
