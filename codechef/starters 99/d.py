import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
go from most to least important bit
include all with bit in group 1
if it results in completed group, impossible,
UNLESS group 1 already has elements AND bit elements are all
exclusive
then rest go to group 2, and then
8 8 5 5 1
x contains bit i if x or i == x
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    if ar.count(0) != 0: #0 in one group and the rest in other
        ans = 0
        for ii in ar:
            ans = ans | ii
        print(ans)
    else:
        m = max(ar)
        if ar.count(m) == n: print(0) #everything is same?
        else:
            h = [5353535353535353535353535353535353535353]*n
            b = 1
            while b <= m:
                b *= 2
            b //= 2
            ss = n
            ml = b
            while b != 0:
                c = 0
                exclusive = 5353535353535353535353535353535353535353
                for j in range(n):
                    if ar[j] | b == ar[j]:
                        if h[j] == 5353535353535353535353535353535353535353: c += 1
                        elif exclusive == 5353535353535353535353535353535353535353: exclusive = h[j]
                        else: exclusive = max(exclusive,h[j])
                """
                exclusive and complete: break, groups decided
                exclusive not complete: set to alt group?
                not exclusive but complete: skip
                not exclusive not complete: merge to main group
                
                """
                if c != ss and exclusive != 5353535353535353535353535353535353535353: #transfer to group 1
                    ss -= c
                    for k in range(n):
                        if ar[k] | b == ar[k]: h[k] = exclusive
                elif exclusive == 5353535353535353535353535353535353535353 and c != ss:
                    ss -= c
                    for rr in range(n):
                        if ar[rr] | b == ar[rr]: h[rr] = b
                        
                elif exclusive == 5353535353535353535353535353535353535353 and c == ss and ss != n: break #special case
                b //= 2
            g0,g1 = 0,0
            mm = min(h)
            #print(h)
            d = {}
            for snth in range(n):
                xx = h[snth]
                if d.get(xx) == None: d[xx] = ar[snth]
                else: d[xx] = d[xx] | ar[snth]
            er = list()
            for sn in d.keys():
                er.append(d[sn])
            er.sort()
            for ff in range(1,len(er)):
                g1 = g1 | er[ff]
            print(er[0] ^ g1)
                    
        
