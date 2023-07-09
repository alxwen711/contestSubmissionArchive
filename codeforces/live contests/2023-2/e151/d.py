import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
idea is to place it before a rating loss
can use dp to track how much final gain occurs
find the height of before each drop, test only those
following a ramping mechanism
ie. if the floor is for a later round, it much be
higher in value
can also use a running sum build to calc final result
given index as line, how to calc final total?
"""

def solve(n,ar):
    rs = [0]*n
    score = 0
    debt = 0
    inc = True
    for i in range(n):
        if ar[-i-1] < 0: debt -= ar[-i-1]
        else:
            inc = max(ar[-i-1]-debt,0)
            score += inc
            debt -= (ar[-i-1]-inc)
        rs[-i-1] = score
    tested = False
    score = 0
    high = -1
    best = -999999999999999999
    ans = 100000000000000000
    for j in range(n):
        if ar[j] < 0 and score > high:
            high = score
            fs = score
            if j != n-1: fs += rs[j+1]
            if fs > best:
                best = fs
                ans = score
        score += ar[j]
    #print(rs)
    return ans

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
