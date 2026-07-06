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
    ar = readar()
    br = readar()
    br.sort()
    ans = sum(ar)
    index = 0
    ar.sort()
    ar.reverse()
    for b in br:
        index += b
        if index > n: break
        ans -= ar[index-1]
    print(ans)
