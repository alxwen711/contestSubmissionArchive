import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def create_sparse(ar,lar,n,m):
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= lar:
        tmp = list()
        for i in range(n-dist+1):
            tmp2 = list()
            for j in range(m-dist+1):
                #find [i:i+dist]
                tmp2.append(min(s[prevrow][i][j],s[prevrow][i+dist//2][j],s[prevrow][i][j+dist//2],s[prevrow][i+dist//2][j+dist//2]))
            tmp.append(tmp2)
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def query(l: int, h: int, ar: list, length: int):
    #l,h is the starting coordinate
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l][h]
    else:
        inc = length-two
        return min(ar[ex][l][h],ar[ex][l+inc][h],ar[ex][l][h+inc],ar[ex][l+inc][h+inc])

def solve(ar,n,m):
    low = 1
    high = min(n,m)
    s = create_sparse(ar,high,n,m)
    while high-low > 1:
        mid = (low+high)//2
        test = False
        for a in range(n-mid+1):
            for b in range(m-mid+1):
                if query(a,b,s,mid) >= mid:
                    test = True
                    break
            if test:
                break
        if test: low = mid
        else: high = mid
    test = False
    for c in range(n-high+1):
        for d in range(m-high+1):
            if query(c,d,s,high) >= high:
                test = True
                break
        if test:
            break
    if test: return high
    else: return low
        
for i in range(readint()):
    n,m = readints()
    ar = list()
    for j in range(n):
        tmp = readar()
        ar.append(tmp)
    print(solve(ar,n,m))
    
