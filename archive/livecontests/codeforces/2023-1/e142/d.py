import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def ll(x):
    d = {}
    for i in range(len(x)):
        d[x[i]] = i
    return d

for i in range(readint()):
    n,m = readints()
    ar = list()
    for j in range(n):
        tmp = readar()
        ar.append(tmp)
    ans = list()
    d = {}
    for k in range(n):
        base = "*"*m
        loc = ll(ar[k])
        for l in range(1,m+1):
            q = loc[l]
            if l == 10: base = base[:q]+"0"+base[q+1:]
            else: base = base[:q]+str(l)+base[q+1:]
            d[base] = 1
        #if k == 0: print(base)
    for t in range(n):
        s = "*"*m
        a = 0
        for u in range(m):
            q = ar[t][u]-1
            if u == 9: s = s[:q]+"0"+s[q+1:]
            else: s = s[:q]+str(u+1)+s[q+1:]
            if d.get(s) == None: break
            else: a += 1
        ans.append(a)
    print(*ans)
