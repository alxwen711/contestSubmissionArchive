import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,q,g = readints()
    d = {}
    s = {}
    for _ in range(q):
        ar = list(readins())
        if ar[0] == "Q":
            print(d.get(int(ar[1]),0))
        else:
            v = int(ar[2])
            g = int(ar[1])
            for k in range(3,3+v):
                p = int(ar[k])
                if s.get(p) == None:
                    s[p] = g
                    if d.get(g) == None: d[g] = 0
                    d[g] += 1
                else:
                    d[s[p]] -= 1
                    if d.get(g) == None: d[g] = 0
                    d[g] += 1
                    s[p] = g
        
