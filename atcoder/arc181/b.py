import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there are more scenarios not being considered here
"""

def chain(s,i,n):
    if i == 1: return True
    inv = n//i
    for a in range(inv):
        v = s[a]
        for b in range(a,n,inv):
            if s[b] != v: return False
    return True

for _ in range(readint()):
    s = readin()
    n = len(s)
    x = readin()
    y = readin()
    x0,y0 = x.count("0"),y.count("0")
    x1,y1 = len(x)-x0,len(y)-y0
    #print(x0,x1,y0,y1)
    flag = False
    if x0 == y0: flag = True
    elif x1 != y1:
        for i in range(1,n+1):
            if n % i == 0:
                if chain(s,i,n):
                    diff = (x0-y0)*i
                    if diff % (y1-x1) == 0 and diff // (y1-x1) > 0:
                        flag = True
                        break
                    #if x0*i+x1 == y0*i+y1:
                    #    flag = True
                    #    break
    if flag: print("Yes")
    else: print("No")
