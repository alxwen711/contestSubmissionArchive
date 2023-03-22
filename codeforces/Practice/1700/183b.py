import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
figure out which pairs results in a scope seeing double
everything not hit -> 1
test each one hit with the method
"""

def solve(a,b,n,m,x):
    cr = list()
    for i in range(n):
        cr.append(((a[i]-x)*b[i]) % m)
    cr.sort()
    best = 0
    chain = 0
    for j in range(n-1):
        if cr[j] == cr[j+1]: chain += 1
        else: chain = 0
        if chain > best: best = chain
    return best+1

def g(a,b):
    h = a[0]-b[0]
    v = a[1]-b[1]
    if h == 0: return a[0]
    if v == 0: return -1
    if (h*a[1]) % v != 0: return -1
    return a[0]-(h*a[1]//v)
    
mm = 2111511013
n,m = readints()
f = list()
for i in range(m):
    a,b = readints()
    f.append((a,b))

pts = list()
for c in range(m):
    for d in range(m):
        if c != d:
            x = g(f[c],f[d])
            if 1 <= x <= n: pts.append(x)

pts = list(set(pts))
ar = list()
br = list()
for snth in range(m):
    ar.append(f[snth][0])
    br.append(pow(f[snth][1],mm-2,mm))

ans = n-len(pts)
for j in range(len(pts)):
    ans += solve(ar,br,m,mm,pts[j])
    #adjust array
print(ans)
    
