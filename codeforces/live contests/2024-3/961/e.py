import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
with an even number of tables, basic greedy setup
odd number of tables is harder
this might be the dp? with 5 tables:

compute 1/2 and 1/7 scenarios
if 1/2, then next table is 7/?
if 1/7, then next table is 2/?
? in both cases can be either 3 or 8,
take one, then the other value is part of next table
repeat until ? is 5/10, must be paired with 6
only need to compute the best sums leading up to each table

this runs in some linearish runtime

and in typical fashion i completely misread the problem. oops.

chain looping idea still works here, probably redoing this since the code
is an actual cluster now
"""

def optimize(ar,br):
    cr = list()
    for a in ar:
        cr.append((-a[0],a[1]))
    for b in br:
        cr.append((-b[0],b[1]))
    cr.sort()
    dr = list()
    best = cr[0][1]
    dr.append(cr[0])
    for c in range(1,len(cr)):
        if cr[c][1] < best:
            if cr[c][0] == dr[-1][0]: dr.pop()
            dr.append(cr[c])
            best = cr[c][1]
    er = list()
    for dd in dr:
        er.append((-dd[0],dd[1]))
    return er

def listcombine(ar,x):
    br = list()
    for i in br:
        if x > i[1]: br.append((i[0],x))
        elif x < i[0]: br.append((x,i[1]))
        else: br.append((i[0],i[1]))
    return br

def solve(n,ar):
    if n % 2 == 0: # easy scenario
        a,b,c,d = ar[0],ar[1],ar[n],ar[1+n]
        oa,ob = [(min(a+b,c+d),max(a+b,c+d))],[(min(b+c,a+d),max(b+c,a+d))]
        for i in range(1,n//2):
            a,b,c,d = ar[2*i],ar[2*i+1],ar[2*i+n],ar[2*i+1+n]
            oc = optimize(listcombine(listcombine(oa,a+b),c+d),listcombine(listcombine(ob,a+b),c+d))
            od = optimize(listcombine(listcombine(oa,c+b),a+d),listcombine(listcombine(ob,c+b),a+d))
            oa = oc
            ob = od
        ans = 67348734896734896743764376
        for snth in oa:
            ans = min(ans,snth[1]-snth[0])
        for snthi in ob:
            ans = min(ans,snthi[1]-snthi[0])
        return ans
    # odd scenario
    if n == 1: return abs(ar[0]-ar[1])
    config = list()
    config.append((0,1))
    for i in range(n-1):
        nv = (config[-1][1]+n) % (2*n)
        if nv % 2 == 0: config.append((nv,nv+1))
        else: config.append((nv,nv-1))
    # first pair set up (2 cases)
    d = {}
    d[(0,1)] = [((ar[0]+ar[1]),(ar[0]+ar[1]))]
    d[(0,config[1][0])] = [((ar[0]+ar[config[1][0]]),(ar[0]+ar[config[1][0]]))]
    # mid pair set ups (4 cases)
    print(config)
    for i in range(1,n-1):
        nd = {}
        for j in d.keys(): # all of these d values need to be swapped with the previous used pair instead of the current one
            v = d[j]
            if j[1] == config[i][0]: # use config[i-1][1]
                if nd.get((config[i-1][1],config[i][1])) == None:
                    nd[(config[i-1][1],config[i][1])] = listcombine(d[(config[i-1][0],config[i][0])],ar[config[i-1][1]]+ar[config[i][1]])
                else:
                    br = listcombine(d[(config[i-1][0],config[i][0])],ar[config[i-1][1]]+ar[config[i][1]])
                    nd[(config[i-1][1],config[i][1])] = optimize(nd[(config[i-1][1],config[i][1])],br)
                if nd.get((config[i-1][1],config[i+1][0])) == None:
                    nd[(config[i-1][1],config[i+1][0])] = listcombine(d[(config[i-1][0],config[i][0])],ar[config[i-1][1]]+ar[config[i+1][0]])
                else:
                    br = listcombine(d[(config[i-1][1],config[i+1][0])],ar[config[i-1][1]]+ar[config[i+1][0]])
                    nd[(config[i-1][1],config[i+1][0])] = optimize(nd[(config[i-1][1],config[i+1][0])],br)
                
            else: # use config[i][0]
                if nd.get((config[i][0],config[i][1])) == None:
                    nd[(config[i][0],config[i][1])] = listcombine(d[(config[i-1][0],config[i-1][1])],ar[config[i][0]]+ar[config[i][1]])
                else:
                    br = listcombine(d[(config[i-1][0],config[i-1][1])],ar[config[i][0]]+ar[config[i][1]])
                    nd[(config[i][0],config[i][1])] = optimize(nd[(config[i][0],config[i][1])],br)
                if nd.get((config[i][0],config[i+1][0])) == None:
                    nd[(config[i][0],config[i+1][0])] = listcombine(d[(config[i-1][0],config[i-1][1])],ar[config[i][0]]+ar[config[i+1][0]])
                else:
                    br = listcombine(d[(config[i-1][0],config[i-1][1])],ar[config[i][0]]+ar[config[i+1][0]])
                    nd[(config[i][0],config[i+1][0])] = optimize(nd[(config[i][0],config[i+1][0])],br)
        d = nd
    # last pair set up (2 cases)
    nd = {}
    for j in d.keys():
        v = d[j]
        if j[1] == config[-1][0]: 
            if nd.get((config[-2][1],config[-1][1])) == None:
                nd[(config[-2][1],config[-1][1])] = listcombine(d[(config[-2][0],config[-1][0])],ar[config[-2][1]]+ar[config[-1][1]])
            else:
                br = listcombine(d[(config[-2][0],config[-1][0])],ar[config[-2][1]]+ar[config[-1][1]])
                nd[(config[-2][1],config[-1][1])] = optimize(nd[(config[-2][1],config[-1][1])],br)

        else:
            if nd.get((config[-1][0],config[-1][1])) == None:
                nd[(config[-1][0],config[-1][1])] = listcombine(d[(config[-2][0],config[-2][1])],ar[config[-1][0]]+ar[config[-1][1]])
            else:
                br = listcombine(d[(config[-2][1],config[-1][1])],ar[config[-1][0]]+ar[config[-1][1]])
                nd[(config[-1][0],config[-1][1])] = optimize(nd[(config[-1][0],config[-1][1])],br)
    ans = 573475985789574398574385
    for c in nd.keys():
        for e in nd[c]:
            ans = min(ans,e[1]-e[0])
    return ans
    

for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

