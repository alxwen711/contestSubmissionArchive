import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
0n
ppp0
pp0n
pnpp0

ppnpnn0p is not possible
ppnpnn0n is possible

any alternating sequence and then assume negative for the rest
also the start MUST be p

"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    s = sum(ar)-ar[0]
    ab = 0
    best = -s
    for i in range(n-1):
        s -= ar[i+1]
        ab += abs(ar[i])
        best = max(best,ab-abs(ar[0])+ar[0]-s)
    print(best)
