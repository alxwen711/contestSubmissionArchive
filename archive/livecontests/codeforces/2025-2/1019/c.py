import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
obtain 2 subarrays that have medians at most k
median is at most k assuming there are at least 1/2 the values at most k
simplify in 0/1 array, 2 subarrays must have at least 1/2 ones

if L/R has a solution, both just push until valid

if L/M has a solution, then some prefix can be split into 2 valid arrays
R/M is similar with suffix

greedily try and take a segment with half?
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = list()
    for i in ar:
        if i <= k: br.append(1)
        else: br.append(-1)
    #print(br)
    cr = [0] # forwards
    dr = [0] # backwards
    for j in range(n):
        cr.append(cr[-1]+br[j])
        dr.append(dr[-1]+br[-j-1])
    cmin = 4757347598437597345
    dmin = 58934578947589475894
    #print(cr)
    #print(dr)
    for i in range(1,n+1):
        if cr[i] >= 0:
            cmin = i
            break
    for i in range(1,n+1):
        if dr[i] >= 0:
            dmin = i
            break
    #print(cmin,dmin)
    if cmin + dmin < n: print("YES")
    else: # L/M or R/M
        netval = cr[n] # total +/-
        mcr,mdr = [0],[0] # min run vals
        for j in range(1,n+1):
            mcr.append(min(mcr[-1],cr[j]))
            mdr.append(min(mdr[-1],dr[j]))
        #print(mcr,mdr)
        ans = "NO"
        for k in range(1,n-1):
            if cr[k] >= 0:
                rv = netval-cr[k]
                if mdr[n-1-k] <= rv:
                    ans = "YES"
                    break
            if dr[k] >= 0:
                rv = netval-dr[k]
                if mcr[n-1-k] <= rv:
                    ans = "YES"
                    break
        print(ans)
        
