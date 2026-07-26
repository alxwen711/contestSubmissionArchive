import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
O(n^2)

when making the subsequence, left and right rank is just
index in the new list when reading forwards/backwards

sequence can go valid -> invalid -> valid during creation

individually/greedily test what lengths are possible?
this can then determine if an element can be added or not
"""

def f(n,ar,br,cr,dr,k):
    ptr = 1
    for i in range(n):
        if ptr > k: return True
        a,b,c,d = ar[i],br[i],cr[i],dr[i]
        if not ((a <= ptr <= b) or (c <= (k-ptr+1) <= d)): ptr += 1 
    return ptr > k

for _ in range(readint()):
    n = readint()
    ar = list()
    br = list()
    cr = list()
    dr = list()
    for _ in range(n):
        l,r,u,v = readints()
        ar.append(l)
        br.append(r)
        cr.append(u)
        dr.append(v)
    flag = False
    for k in range(n,0,-1):
        if f(n,ar,br,cr,dr,k):
            flag = True
            print(k)
            break
    if not flag: print(0)
