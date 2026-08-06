import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
always remove the highest on a row
only need to keep at most the m highest
(or fewer depending on the best answer found)

lowest row can only use lowest row values
then second lowest must use lowest 2
"""

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    ans = m
    h = list()
    push = 0
    cr = list()
    for j in range(n):
        br = readar() # m values
        br.sort()
        cr.append(br)
    for i in range(n-1,-1,-1):
        req = ar[i]
        if i == n-1:
            for b in cr[-1]:
                heappush(h,b)
                push += b
        else: # try to replace
            for c in cr[i]:
                if len(h) != ans:
                    heappush(h,c)
                    push += c
                elif c > h[0]:
                    v = heappop(h)
                    push -= v
                    heappush(h,c)
                    push += c
        while push-h[0] >= req:
            v = heappop(h)
            push -= v
        ans = min(ans,len(h))
    print(ans)
