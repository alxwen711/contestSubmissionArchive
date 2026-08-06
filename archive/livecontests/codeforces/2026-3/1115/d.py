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
parity -> even/odd
no parities will ever change
10 10 8 4
10 10 6 4
10 6 6 4
10 6 4 4

implied that spamming valid moves until none are
left should result in the optimal sequence

try to just spam sequences?

metric is center - edges, if best case is 0 then get out

operation count can definitely go to some extreme amount

between chains:

+8,+6,+4,+2

+2,+12,-6,-2

these differences are being swapped


26 25 24 21 18 15 8 1
optimization here is possible?
26 19 12 9 6 3 2 1

-1 -1 -3 -3 -3 -7 -7

maybe after the first step we can combine the previous solution??


"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    chain = 2
    for i in range(2,n):
        if ar[i] % 2 == ar[i-2] % 2:
            chain += 1
        else:
            if chain >= 3:
                start = i-chain
                end = i-1
                #print(start,end)
                diffs = list()
                for j in range(start,end):
                    diffs.append(ar[j+1]-ar[j])
                diffs.sort()
                for u in range(len(diffs)):
                    ar[start+u+1] = ar[start+u]+diffs[u]
            chain = 2
    if chain >= 3:
        start = n-chain
        end = n-1
        diffs = list()
        for j in range(start,end):
            diffs.append(ar[j+1]-ar[j])
        diffs.sort()
        for u in range(len(diffs)):
            ar[start+u+1] = ar[start+u]+diffs[u]

    print(*ar)

    
