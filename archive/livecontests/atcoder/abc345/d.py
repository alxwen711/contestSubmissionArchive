import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
do e first, this is literal implementation hell
probably brute forceable by doing largest to smallest
pieces and tracking each currently filled board state
(must be done optimally somehow)

many scenarios with rotational symmetry, want to eliminate these somehow
"""

def vlist(n,h,w,aa,bb,two): #sub gathering process here can be optimized
    ar = list()
    if aa > h or bb > w: return ar
    v = 0
    for x in range(aa):
        for y in range(bb):
            v += two[w*x+y]
    for j in range(h-aa+1):
        for k in range(w-bb+1): #obtain hash value
            ar.append(v*two[j*w+k])
    return ar
def solve():
    n,h,w = readints()
    ar = list()
    xx = 0
    for _ in range(n):
        a,b = readints()
        ar.append((a*b,a,b))
        xx += a*b
    if xx < h*w: return "No"
    ar.sort()
    ar.reverse()
    target = 2**(h*w)-1
    two = [1]
    for _ in range(h*w):
        two.append(two[-1]*2)
    d = {}
    d[0] = 0
    for i in range(n):
        dr = list()
        for dl in d.keys():
            dr.append((d[dl],dl))
        dr.sort()
        #print(d,dr)
        np = {}
        ab,aa,bb = ar[i][0],ar[i][1],ar[i][2]
        cr = vlist(n,h,w,aa,bb,two)
        if aa != bb:
            ddr = vlist(n,h,w,bb,aa,two)
            for e in ddr:
                cr.append(e)
        for c in cr:
            for v in dr:
                #print(dr)
                if (ab + v[0]) > h*w: break
                if v[1] & c == 0:
                    if v[1] | c == target: return "Yes"
                    np[v[1] | c] = 1
        dr.reverse()
        for ddd in dr:
            if (ddd[0]+xx) < h*w: break
            np[ddd[1]] = ddd[0]
        d = np
    return "No"
print(solve())
