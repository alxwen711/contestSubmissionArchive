import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# use dict setup and find num of pair values that can function?
#reduction call to generate min tag

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    d = {}
    for j in range(n):
        a,b = ar[j],br[j]
        q = b//a
        r = a-(b%a)
        #x = q*n+r
        #reduction call
        x = (q,r)
        if d.get(x) == None: d[x] = 0
        d[x] += 1
    ans = 0
    print(d)
    for k in range(n):
        a,b = ar[k],br[k]
        #t = (a-1)*n+b
        t = (a-1,b)
        print(t)
        if d.get(t) != None:
            ans += d[t]
            if a*a == b+b: ans -= 1 #remove same pair
    print(ans//2)
