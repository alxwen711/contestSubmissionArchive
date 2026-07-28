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
    mi,ma = ar[0],ar[0]
    ans = "YES"
    for i in range(1,n):
        x = ar[i]
        if x == mi-1:
            mi -= 1
        elif x == ma+1:
            ma += 1
        else:
            ans = "NO"
            break
    print(ans)
