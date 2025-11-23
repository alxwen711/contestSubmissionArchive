import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
each turn either reduces distance by 1 or 0

options are to mainly to run into a wall and then try to move to a corner?

this problem is irritating

4 cases?
"""

for _ in range(readint()):
    n,a,b,c,d = readints()
    if a == c:
        if b < d: print(d)
        else: print(n-d)
    elif b == d:
        if a < c: print(c)
        else: print(n-c)
    elif a > c and b > d: print(max(n-c,n-d))
    elif a > c and b < d: print(max(n-c,d))
    elif a < c and b > d: print(max(c,n-d))
    elif a < c and b < d: print(max(c,d))
    


    # 1d cases
    """
    if a == c:
        if b < d: print(d)
        else: print(n-d)
    elif b == d:
        if a < c: print(c)
        else: print(n-c)
    elif a < c: # 2d cases
        ans = a
        apos,bpos,cpos,dpos = 0,b,c-a,d
        if b > d:
            dpos += min(a,b-d)
        else:
            dpos -= min(a,b-d)
        # either run down or up
    """ 
