import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m,k = readints()
    ar = readar()
    x = n//k #min val
    freq = m
    if n % k != 0:
        x += 1
        freq = n % k
    mm = max(ar)
    if mm > x: print("NO")
    elif mm < x: print("YES")
    elif ar.count(mm) > freq: print("NO")
    else: print("YES")
