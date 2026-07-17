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
    ar = readar()
    l = ar.index(n)
    r = l
    ans = "YES"
    for i in range(n-1,0,-1):
        x = ar.index(i)
        if x == l-1:
            l -= 1
        elif x == r+1:
            r += 1
        else:
            ans = "NO"
            break
    print(ans)
