import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
set base to -5000000000000000
find minimum maximum
then closest two values
"""

for i in range(readint()):
    n = readint()
    ar = list()
    br = list()
    for j in range(n):
        a,b = readints()
        br.append(min(a,b))
        ar.append((a,j))
        ar.append((b,j))
    ar.sort()
    br.sort()
    lowest = br[-2]
    sl = br[-1]
    ans = 34678794659747659247659274
    for k in range(len(ar)-1):
        if ar[k][1] != ar[k+1][1] and min(ar[k][0],ar[k+1][0]) >= lowest and max(ar[k][0],ar[k+1][0]) >= sl:
            ans = min(ans,abs(ar[k][0]-ar[k+1][0]))
    print(ans)
