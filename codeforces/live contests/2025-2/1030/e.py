import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
corners will likely be last?
try doing a sudoku like search
"""
from random import randint
def search(ar,br,n,m,x):
    if x > n*m: # filled grid, print answer
        print("Answer found:")
        cr = list()
        for i in range(n):
            for j in range(m):
                cr.append((ar[i][j],i,j))
        cr.sort()
        dr = list()
        for c in cr:
            dr.append((c[1]+1,c[2]+1))
        print(dr)
        return 1
    else:
        for i in range(n):
            for j in range(m):
                if ar[i][j] == 0 and (x != 1 or i != 0 or j >= 2): #confirm viability
                    mh = 1
                    hl = list()
                    for l in range(n):
                        for y in range(m):
                            if ar[l][y] != 0:
                                dist = abs(l-i)+abs(y-j)
                                if dist > mh:
                                    mh = dist
                                    hl = [(l,y)]
                                elif dist == mh:
                                    hl.append((l,y))
                    flag = True
                    for k in hl:
                        if br[k[0]][k[1]] == 3:
                            flag = False
                            break
                    if flag:
                        ar[i][j] = x
                        for u in hl:
                            br[u[0]][u[1]] += 1
                        v = search(ar,br,n,m,x+1)
                        for u in hl:
                            br[u[0]][u[1]] -= 1
                        ar[i][j] = 0
                        if v == 1 and x != 1: return 1
    return 0
n = 5
m = 5

ar = list()
br = list()
for _ in range(n):
    tmp = [0]*m
    tmp2 = [0]*m
    ar.append(tmp)
    br.append(tmp2)

search(ar,br,n,m,1)
