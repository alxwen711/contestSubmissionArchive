import sys
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
square moving is fastest method
144 -> 23 moves
"""

def f(c,a,b):
    return (a+c-1)//c+(b+c-1)//c+(c-1)

for i in range(readint()):
    a,b = readints()
    low = 1
    high = max(a,b)
    while high-low > 1000:
        diff = (high-low)//3
        m1 = low+diff
        m2 = low+diff*2
        x = f(m1,a,b)
        y = f(m2,a,b)
        if x == y:
            low = m1
            high = m2
        elif x < y:
            high = m2
        else: low = m1
    best = 97535468569876398428957892758
    for j in range(low,high+1):
        best = min(best,f(j,a,b))
    print(best)
    """
    ar = list()
    if a == 1 and b == 15:
        for ii in range(1,20):
            ar.append(f(ii,a,b))
    print(ar)
    """
