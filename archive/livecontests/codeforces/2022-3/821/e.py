import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
each tile has some sort of 2**n cycle length
0 x: x + 2**x
x 0: (2**x + n - 1) + 2**x
"""
def update(d,ar,t):
    for w in range(36):
        if ar[w//6][w%6] == 1:
            #d[w].append(str(bin(t))[2:])
            d[w].append(t)

    
ar = list()
br = list()
d = {}
for i in range(6):
    ar.append([0]*6)
    br.append([0]*6)
    for j in range(6):
        d[i*6+j] = list()

for k in range(51):
    ar[0][0] = 1
    update(d,ar,k)
    cr = list()
    for sth in range(6):
        cr.append([0]*6)
    for s in range(6):
        for t in range(6):
            if ar[s][t] == 1:
                if br[s][t] == 0:
                    br[s][t] = 1
                    if t != 5: cr[s][t+1] = 1
                else:
                    br[s][t] = 0
                    if s != 5: cr[s+1][t] = 1
    ar = cr
    
for f in range(36):
    print(f//6,f%6,d[f])
                    
                    

