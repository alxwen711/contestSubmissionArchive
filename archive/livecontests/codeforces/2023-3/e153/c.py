import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
track most left winning and losing elements
winning if only losing to left
losing if no losing to left or winning to left
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    for j in range(n):
        br.append((ar[j],j))
    loss = 10000000000000
    win = 10000000000000
    ans = 0
    br.sort()
    for k in br:
        if k[1] < loss: # no l to left
            loss = k[1]
        elif k[1] < win: #no w to right
            ans += 1
            win = k[1]
        #otherwise w to left, counts as l
    print(ans)
    
    
