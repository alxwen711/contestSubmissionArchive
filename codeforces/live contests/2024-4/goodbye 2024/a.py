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
    #ar.sort()
    ans = "NO"
    for i in range(n-1):
        if min(ar[i],ar[i+1])*2 > max(ar[i],ar[i+1]):
            ans = "YES"
            break
    print(ans)
