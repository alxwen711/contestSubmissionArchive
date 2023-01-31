import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if 1 is part of death path, anything not changing it is allowed
if it isn't 1+route can redirect to possible dead routes
also track out of bounds values
"""

def trackdead(n,ar):
    d = {}
    dead = list()
    a = [0]*n
    for i in range(n):
        x = i+ar[i]
        if x < 0 or x >= n:
            dead.append(i)
            a[i] = 1
        else:
            if d.get(x) == None: d[x] = list()
            d[x].append(i)
    while len(dead) != 0:
        y = dead.pop()
        if d.get(y) != None:
            for j in range(len(d[y])):
                if a[d[y][j]] == 0:
                    a[d[y][j]] = 1
                    dead.append(d[y][j])
    return a,sum(a)

def path(n,ar):
    h = [0]*n
    node = 0
    c = 0
    f = {}
    while True:
        if node < 0 or node >= n: return c,True,f
        if h[node] == 1: return c,False,f
        f[node] = c
        h[node] = 1
        c += 1
        node += ar[node]

def loopback(stpath,pl,n,ar):
    d = {}
    for t in range(n):
        if stpath.get(t) == None:
            if d.get(ar[t]+t) == None: d[ar[t]+t] = list()
            d[ar[t]+t].append(t)
    sub = 0
    cr = list(stpath.keys())
    a = [0]*n
    for i in range(len(cr)):
        x = cr[i]
        subval = pl-stpath[x]
        q = list()
        q.append(x)
        while len(q) != 0:
            y = q.pop()
            a[y] = 1
            if d.get(y) != None:
                for u in range(len(d[y])):
                    if a[d[y][u]] == 0:
                        q.append(d[y][u])
                        sub += subval
    return sub
for i in range(readint()):
    n = readint()
    ar = readar()
    h,deadcount = trackdead(n,ar)
    pl,deadst,stpath = path(n,ar)
    #print(pl,deadst)
    ans = 0
    if deadst: #stpath is dead
        ans += (2*n+1)*(n-pl) #not on path to anything,7
        ans += pl*(deadcount-pl) #path to dead path
        ans -= loopback(stpath,pl,n,ar)#if non deadcount maps back to path, then problem
        ans += pl*(n+1) #path out of bounds
        ans += (pl*pl-pl)//2 #path to later in path
    else: #stpath is not dead
        ans += pl*deadcount # path to dead path
        ans += pl*(n+1) #path out of bounds
    print(ans)
