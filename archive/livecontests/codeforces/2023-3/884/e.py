import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
impossible setups:
crossing diagonals
"""

for i in range(readint()):
    n,m,k = readints()
    ans = "YES"
    dd = {}
    for j in range(k):
        a,b,c,d = readints()
        if dd.get((a,b,c,d)) != None:
            ans = "NO"
        dd[(a,d,c,b)] = 7
    print(dd)
    print(ans)
    
