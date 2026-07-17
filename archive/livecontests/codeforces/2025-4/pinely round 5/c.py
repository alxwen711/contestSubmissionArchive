import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
also has to determine the optimal order
optimally want to cross X with only expensive items
most expensive item costs X
"""

for _ in range(readint()):
    n,x = readints()
    ar = readar()
    ar.sort()
    lp = 0
    hp = n-1
    ans = 0
    br = list()
    r = 0
    for _ in range(n):
        if (r + ar[hp]) >= x:
            ans += ar[hp]
            br.append(ar[hp])
            r = (r+ar[hp]) % x
            hp -= 1
        else:
            br.append(ar[lp])
            r += ar[lp]
            lp += 1
    print(ans)
    print(*br)
    
