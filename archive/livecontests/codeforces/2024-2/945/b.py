import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = s[prevrow][i] | s[prevrow][i+dist//2]
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s


def query(l: int, h: int, ar: list):
    length = h-l+1
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
    if length == two: return ar[ex][l]
    else: return ar[ex][l] | ar[ex][h-two+1]

def f(x,n,sparse):
    v = query(0,0+x-1,sparse)
    for i in range(n-x):
        if query(i+1,i+x,sparse) != v: return False
    return True

for _ in range(readint()):
    n = readint()
    ar = readar()
    sparse = create_sparse(ar)
    low = 1
    high = n
    while high-low > 1:
        mid = (low+high)//2
        if f(mid,n,sparse): high = mid
        else: low = mid
    if f(low,n,sparse): print(low)
    else: print(high)
