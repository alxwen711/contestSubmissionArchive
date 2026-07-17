import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 2 3 4 5
1 2 3, 2 3 4, 3 4 5
at most 2 increments on each element
2,3,10,25,12,7,10,12,1,46
2,3,10,26,12,7,11,12,1,47
0,2,2,2,2,2,2,2

"""

def f(n,ar):
    """
    br = list()
    s = sum(ar[:2])
    for i in range(2,n):
        s += ar[i]
        br.append(s % 3)
        s -= ar[i]
    if n == 3: return (3-br[0]) % 3
    elif n == 4: return max((3-br[0]) % 3, (3-br[1]) % 3)
    """
    br = list()
    cr = [0]
    ans = 0
    s = 0
    for k in range(n):
        br.append(ar[k])
        s += ar[k]
        if k >= 2:
            while s % 3 != 0:
                br[-1] += 1
                s += 1
                ans += 1
            s -= br[k-2]
            cr.append(ans)
    #print(br)
    return cr

for i in range(readint()):
    n = readint()
    ar = readar()
    a = f(n,ar)
    ar.reverse()
    b = f(n,ar)
    ans = 875987298572398573985
    nv = len(a)
    for j in range(nv):
        ans = min(ans,a[j]+b[nv-1-j])
    print(ans)
