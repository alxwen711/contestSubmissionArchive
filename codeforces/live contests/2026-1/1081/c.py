import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
figure out the cycle count, then determine how many
extra seconds needed
"""

for _ in range(readint()):
    n,h,k = readints()
    ar = readar()
    m = [0]*(n+1)
    m[n-1] = ar[-1]
    for i in range(n-2,-1,-1):
        m[i] = max(m[i+1],ar[i])
    br = list()
    rt = 0 # prefix
    mv = 9999999999999999999999
    for j in range(n):
        mv = min(mv,ar[j])
        rt += ar[j]
        br.append(rt+max(0,m[j+1]-mv))
    s = sum(ar)
    c = (h-1)//s
    ans = c*(n+k)
    r = h-(c*s)
    for snth in range(n):
        ans += 1
        if r <= br[snth]: break
    print(ans)
