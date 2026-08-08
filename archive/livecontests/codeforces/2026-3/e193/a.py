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
    v = n+1 # must be prime?
    ans = "YES"
    for i in range(2,v+1):
        if i*i > v: break
        if v % i == 0:
            ans = "NO"
            break
    print(ans)
