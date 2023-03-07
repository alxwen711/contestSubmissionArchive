import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = list()
    br = list()
    ans = 0
    for j in range(n):
        a,b = readints()
        ar.append(a)
        br.append(b)
    if ar.count(k) != 0 and br.count(k) != 0: print("YES")
    else: print("NO")
