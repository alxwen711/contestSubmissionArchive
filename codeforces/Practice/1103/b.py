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
    ans = "YES"
    for i in range(k):
        v = 0
        for j in range(i,n,k):
            if s[j] == "1": v += 1
        if v % 2 == 1:
            ans = "NO"
            break
    print(ans)
