import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    ans = sum(ar)
    ar.sort()
    st = [0]*(k+1)
    ed = [0]*(k+1)
    ai = 0
    bi = n-1
    a,b = 0,0
    for j in range(1,k+1):
        a += ar[ai]
        a += ar[ai+1]
        b += ar[bi]
        st[j] = a
        ed[j] = b
        ai += 2
        bi -= 1
    best = 8947589233253253253253254389579
    for u in range(k+1):
        best = min(best,st[u]+ed[k-u])
    print(ans-best)
