import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def hashstr(s):
    n = len(s)
    m = 1666666667
    ar = [0]*(n+1)
    br = [0]*(n+1)
    a,b = 0,0
    for i in range(n):
        a *= 29
        b *= 29
        a += (ord(s[i])-96)
        b += (ord(s[-i-1])-96)
        a = a % m
        b = b % m
        ar[i+1] = a
        br[i+1] = b
    return ar,br
        

n,s = map(str,sys.stdin.readline().split())
n = int(n)
nn = len(s)
ar,br = hashstr(s)
ans = list()
for i in range(n):
    t = sys.stdin.readline()[:-1]
    x = len(t)
    if x == nn: #must be same length or 1 replace
        diff = 0
        for j in range(nn):
            if t[j] != s[j]: diff += 1
        if diff <= 1: ans.append(i+1)
    elif x == nn-1: #deleted 1
        cr,dr = hashstr(t)
        for u in range(nn):
            if cr[u] == ar[u] and dr[nn-u-1] == br[nn-u-1]:
                ans.append(i+1)
                break
    elif x == nn+1:
        cr,dr = hashstr(t)
        for v in range(nn+1):
            if cr[v] == ar[v] and dr[nn-v] == br[nn-v]:
                ans.append(i+1)
                break
print(len(ans))
print(*ans)



        
