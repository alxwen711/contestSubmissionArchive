import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if a beautiful segment is sorted, each value is some
integral value multiplied by the previous
ie. must be same or double or triple previous
use a "base" lowest value, then from largest to smallest
run a sort of dp build
"""


for i in range(readint()):
    n = readint()
    ar = readar()
    m = max(ar)
    h = [0]*(m+1)
    for a in ar:
        h[a] += 1
    cl = [0]*(m+1)
    ans = 0
    for j in range(m,0,-1):
        if h[j] != 0: #can actually base a chain here
            length = h[j]+cl[j]
            ans = max(ans,j*length)
            #1 case
            cl[1] = max(cl[1],length)
            b = 2
            while b*b <= j:
                if j % b == 0: #try update
                    cl[b] = max(cl[b],length)
                    cl[j//b] = max(cl[j//b],length)
                b += 1
    print(ans)
