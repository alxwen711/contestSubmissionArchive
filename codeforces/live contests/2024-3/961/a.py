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
    ar = list()
    for i in range(n):
        ar.append(i+1)
        if i != n-1: ar.append(i+1)
    ans = 0
    for j in range(2*n-1):
        if k <= 0: break
        ans += 1
        k -= ar[-j-1]
        
    print(ans)
