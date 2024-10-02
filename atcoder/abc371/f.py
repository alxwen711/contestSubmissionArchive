import sys
#rom math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
need some method of tracking clusters

Problem G
build each cycle based on the permutation loops
track length of each cycle, AND minimum
starting from frontmost cycle, greedily select best possible
greedily in that it cannot contradict previous cycle modulos
"""

def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        m = n
        n = r
        return gcd(m, n)

n = readint()
ar = readar()
br = readar()
loops = list()
indexes = list()
ans = [0]*n
for ii in range(n):
    ar[ii] -= 1
idv = [-1]*n
for i in range(n):
    if idv[i] == -1:
        c = len(loops) 
        cr = [br[i]]
        dr = [i]
        idv[i] = c
        nv = ar[i]
        while br[nv] != cr[0]:
            idv[nv] = c
            cr.append(br[nv])
            dr.append(nv)
            nv = ar[nv]
        loops.append(cr)
        indexes.append(dr)
#print(loops)
#print(indexes)
#print(idv)
cycles = {}
h = [1]*len(loops)
for k in range(n):
    if h[idv[k]] == 1: # compute loop
        er = list()
        index = idv[k]
        nn = len(loops[index])
        for iii in range(nn):
            er.append((loops[index][iii],iii))
        er.sort()
        for e in er:
            flag = True
            sf = False
            for f in cycles.keys():
                if f == nn:
                    sf = True
                    if cycles[f] != e[1]:
                        flag = False
                    break
                else: # change somewhere around here to use crt
                    g = gcd(f,nn)
                    if cycles[f] % g != e[1] % g:
                        flag = False
                        break
            if flag: # run this
                for l in range(nn):
                    ans[indexes[index][l]]= loops[index][(l+e[1]) % nn]
                if not sf:
                    cycles[nn] = e[1]
print(*ans)
