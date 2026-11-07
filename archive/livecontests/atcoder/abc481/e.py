import sys
from decimal import Decimal, getcontext

getcontext().prec = 20

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
max range is 180 degrees
almost definitely a float point problem here.
possibly use direct comparisons?
most likely have to use quadrant scenarios

"""
def quadrant(y,x):
    if x > 0 and y >= 0: # Q1
        return (1,Decimal(y)/Decimal(x))
    elif x <= 0 and y > 0: # Q2
        return (2,Decimal(-x)/Decimal(y))
    elif x < 0 and y <= 0: # Q3
        return (3,Decimal(y)/Decimal(x))
    else: # Q4
        return (4,Decimal(-x)/Decimal(y))

def aboverange(a,b):
    if b[0]-a[0] <= 1: return False
    if b[0]-a[0] >= 3: return True
    if a[1] > b[1]: return False
    return True

anslist = list()
for _ in range(readint()):
    n = readint()
    ar = list()
    br = [[],[],[],[]]
    for _ in range(n):
        x,y = readints()
        q,v = quadrant(y,x)
        br[q-1].append(v)

    for a in range(4):
        br[a].sort()
        for b in br[a]:
            ar.append((a,b))
    for a in range(4):
        for b in br[a]:
            ar.append((a+4,b))
    ptr = 0
    if n <= 2:
        anslist.append(n)
        continue
    ptr = 0
    ans = 0
    for j in range(2*n):
        while aboverange(ar[ptr],ar[j]):
            ptr += 1
        ans = max(ans,j-ptr+1)
    anslist.append(ans)

sys.stdout.write("\n".join(map(str,anslist)))
