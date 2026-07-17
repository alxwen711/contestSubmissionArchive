import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
is simple backtrack fast enough? approx 4000 factors are possible
that said, first step will remove a lot of these factors, only up
to 20 steps are needed to process
"""

def hasZero(n):
    s = str(n)
    for j in range(len(s)):
        if s[j] == "0": return False
    return True

def pal(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-i-1]: return False   
    return hasZero(n)

def f(n,x):
    # check for initial pal
    if pal(n): return [n]
    while x*x <= n:
        if n % x == 0 and hasZero(x):
            inv = int(str(x)[::-1])
            if (n//x) % inv == 0:
                nv = (n//x)//inv
                br = f(nv,x)
                if br != -1:
                    br.append(inv)
                    br.append(x)
                    return br
        x += 1
    return -1
        

n = readint()

ar = f(n,2)
if ar == -1: print(-1)
else:
    ar.reverse()
    br = list()
    cr = list()
    for ii in range(len(ar)):
        if ii % 2 == 0: br.append(str(ar[ii]))
        else: cr.append(str(ar[ii]))
    cr.reverse()
    for c in cr:
        br.append(c)
    print("*".join(br))
        
