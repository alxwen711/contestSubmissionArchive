import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
ar vals only go up to 32767
n^2 can't work, 10^10 is too many operations
find all palindromes first, compute all possible pairs,
then freq ar to get total pair vals?
361 mill operations is too high
about 80 million give or take with this method
"""

def p(x):
    x = str(x)
    for snth in range(len(x)//2):
        if x[snth] != x[-snth-1]: return False
    return True

pal = list()
for i in range(1,32768):
    if p(i): pal.append(i)

for ithuodth in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*32768
    ans = n
    d = {}
    for t in ar:
        h[t] += 1
        ans += (h[t]-1)
        d[t] = 1
    vv = 0
    for v in d.keys():
        m = h[v]
        for u in pal:
            vv += m*h[u^v]
    ans += (vv//2)
    print(ans)
