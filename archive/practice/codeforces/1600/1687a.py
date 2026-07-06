import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def limit(n,k):
    return (n*n-n)//2+(k-n)*(n-1)+(k-n)

def sub(ar,k):
    best = sum(ar[:k])
    x = best
    for j in range(k,len(ar)):
        x += ar[j]
        x -= ar[j-k]
        best = max(best,x)
    return best


for i in range(readint()):
    n,k = readints()
    ar = readar()
    if k <= n: print(sub(ar,k)+((k*k-k)//2))
    else:
        ans = sum(ar)
        ans += limit(n,k)
        print(ans)
