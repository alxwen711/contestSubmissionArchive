import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
sorted with two adjacent numbers swapped
"""

def solve(n,ar):
    ans = 0
    ccccc = False
    loc = [0]*(n+1)
    for hhh in range(n):
        loc[ar[hhh]] = hhh
    #check if an inversion can be kept
    for snth in range(n-1):
        if ar[snth] == snth+2 and ar[snth+1] == snth+1:
            ccccc = True
            break
    #try and find a starting point for inversion
    if not ccccc:
        inta,intb = -1,-1
        for c in range(n):
            if c != 0:
                if ar[c] == c:
                    #try c-1,c
                    v = loc[c+1]
                    inta,intb = c-1,v
                    if v+1 == ar[c-1]: break #optimal case
            if c != n-1:
                if ar[c] == c+2:
                    #try c,c+1
                    v = loc[c+1]
                    inta,intb = c+1,v
                    if v+1 == ar[c+1]: break #optimal case
    #use above for possible start point
        if inta != -1:
            ans += 1
            tmp = ar[inta]
            ar[inta] = ar[intb]
            ar[intb] = tmp
            ccccc = True
    #print(*ar)
    #cycle sweep, check if any case has a cycle with two adjacent values
    hit = [0]*(n+1)
    colour = 0
    for i in range(n):
        if hit[ar[i]] == 0:
            colour += 1
            cycle = -1
            pt = ar[i]
            while hit[pt] == 0:
                hit[pt] = colour
                cycle += 1
                pt = ar[pt-1]
            ans += cycle
    for tt in range(n-1):
        if hit[tt+1] == hit[tt+2]: ccccc = True
    if ccccc: ans -= 1
    else: ans += 1
    return ans


for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
