import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(a,b,c,x):
    #check how many crickets are together
    if a == x or b == x or c == x: return "YES"
    p = a
    f = b
    g = c
    if abs(a[0]-c[0])+abs(a[1]-c[1]) == 2:
        p = b
        f = a
        g = c
    if abs(a[0]-b[0])+abs(a[1]-b[1]) == 2:
        p = c
        f = a
        g = b
    if (p[0] == 1 or p[0] == n) and (p[1] == 1 or p[1] == n): #corner case
        if p[0] == x[0] or p[1] == x[1]: return "YES"
        else: return "NO"
    duo = (f[0]+f[1]) % 2 #0 light 1 dark
    sing = (duo + 1) % 2
    if (x[0]+x[1]) % 2 == duo: return "YES"
    elif abs(x[0]-p[0]) % 2 == 0 and abs(x[1]-p[1]) % 2 == 0: return "YES"
    return "NO"
    

    
for i in range(readint()):
    n = readint()
    a,b,c,d,e,f = readints()
    x,y = readints()
    print(solve([a,b],[c,d],[e,f],[x,y]))
    
