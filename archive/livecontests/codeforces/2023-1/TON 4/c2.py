import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# fuck me for thinking this had to be increasing subsequence
for i in range(readint()):
    n,c,d = readints()
    ar = readar()
    br = list(set(ar))
    pen = (len(ar)-len(br))*c
    ar = br
    ar.sort()
    best = 8932798274983274
    x = len(ar)
    #print(ar)
    for j in range(x):
        #if n == 6: print(j,(ar[j]-j-1)*d+c*(x-j-1)+pen)
        best = min(best,(ar[j]-j-1)*d+c*(x-j-1))
    print(min(best+pen,c*n+d))
