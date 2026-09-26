import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy is to find a set
hard is to find number of sets

for easy part, use some sort of greedy??

0 3 2 2 2 1
0 -> nothing in 0
3 -> something in 0-1,2-3,4-5,nothing in 6 (not that that's possible)
2 -> something in 0-2 and 3-5
.
.
1 -> something in 0-5

start from full set, determine what has to be removed
(counting would then be what could be removed?)
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    conditions = list()
    for i in range(n):
        l = ar[i]*(i+1)
        h = l+i+1
        conditions.append((l,1))
        conditions.append((h,-1))
    conditions.sort()
    ans = list()
    ptr = 0
    p = 0
    for j in range(n):
        while ptr < len(conditions):
            if conditions[ptr][0] <= j:
                p += conditions[ptr][1]
                ptr += 1
            else: break
        if p == 0:
            ans.append(j)
    print(len(ans))
    print(*ans)
