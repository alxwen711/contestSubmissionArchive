import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
a,b is start pos
c,d is crate pos
e,f is finish pos
"""
def dist(ar,inc):
    x = 0
    for i in range(3):
        x += abs(ar[i][0]-ar[i+1][0])
        x += abs(ar[i][1]-ar[i+1][1])
    if inc: x += 2
    return x

def solve(a,b,c,d,e,f):
    if c == e and d == f: return 0
    if c == e: #only vertical move
        if d < f: #push up
            ans = f-d
            ans += abs(c-a)
            ans += abs(b-(d-1))
            if a == c and b > d: ans += 2
        else: #push down
            ans = d-f
            ans += abs(c-a)
            ans += abs(b-(d+1))
            if a == c and d > b: ans += 2
        return ans
    if d == f: #only horizontal move
        if c < e: #push right
            ans = e-c
            ans += abs(d-b)
            ans += abs(a-(c-1))
            if b == d and a > c: ans += 2
        else: #push left
            ans = c-e
            ans += abs(d-b)
            ans += abs(a-(c+1))
            if b == d and c > a: ans += 2
        return ans
    #two cases hor->ver and ver->hor
    hor = e-c
    ver = f-d
    ar = list()
    br = list()
    ainc = False
    binc = False
    if hor > 0 and ver > 0:
        ar = [(a,b),(c-1,d),(e,d-1),(e,f-1)]
        br = [(a,b),(c,d-1),(c-1,f),(e-1,f)]
        if b == d and a > c: ainc = True
        if a == c and b > d: binc = True
    elif hor > 0:
        ar = [(a,b),(c-1,d),(e,d+1),(e,f+1)]
        br = [(a,b),(c,d+1),(c-1,f),(e-1,f)]
        if b == d and a > c: ainc = True
        if a == c and b < d: binc = True
    elif ver > 0:
        ar = [(a,b),(c+1,d),(e,d-1),(e,f-1)]
        br = [(a,b),(c,d-1),(c+1,f),(e+1,f)]
        if b == d and a < c: ainc = True
        if a == c and b > d: binc = True
    else:
        ar = [(a,b),(c+1,d),(e,d+1),(e,f+1)]
        br = [(a,b),(c,d+1),(c+1,f),(e+1,f)]
        if b == d and a < c: ainc = True
        if a == c and b < d: binc = True
    return min(dist(ar,ainc),dist(br,binc))
        
a,b,c,d,e,f = readints()

print(solve(a,b,c,d,e,f))
