import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
3x3 onwards has a lot more flex in the subrectangles

111
102
120

maybe possible to just greed through this?
"""

for _ in range(readint()):
    n,m = readints()
    ar = list()
    for _ in range(n):
        s = readin()
        tmp = list()
        for i in s:
            tmp.append(int(i))
        ar.append(tmp)
    br = list()
    for _ in range(n):
        s = readin()
        tmp = list()
        for i in s:
            tmp.append(int(i))
        br.append(tmp)
    for a in range(n-1):
        for b in range(m-1):
            if (br[a][b]-ar[a][b]) % 3 == 1: # add 1 case
                ar[a][b] = (ar[a][b]+1) % 3
                ar[a+1][b+1] = (ar[a+1][b+1]+1) % 3
                ar[a][b+1] = (ar[a][b+1]+2) % 3
                ar[a+1][b] = (ar[a+1][b]+2) % 3
            elif (br[a][b]-ar[a][b]) % 3 == 2: # add 2 case
                ar[a][b] = (ar[a][b]+2) % 3
                ar[a+1][b+1] = (ar[a+1][b+1]+2) % 3
                ar[a][b+1] = (ar[a][b+1]+1) % 3
                ar[a+1][b] = (ar[a+1][b]+1) % 3
    ans = "YES"
    for c in range(n):
        if ar[c][-1] != br[c][-1]: ans = "NO"
    for d in range(m):
        if ar[-1][d] != br[-1][d]: ans = "NO"
    print(ans)
