import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ask any of the first n-1 values if the AND value is 0
only the last value of the permutation has to be determined

ask n-1 times, then n-1//2, then n-1//4

ask everything if the 1 bit is present, then depending on diff
the last value's 1 bit can be determined

this should eliminate enough values, then try asking for 2 bit
then 4 bit, and so on, until only 1 candidate is remaining
"""

def solve(n):
    indexvals = [i for i in range(1,n)]
    candidates = [i for i in range(1,n+1)]
    base = 1
    while len(candidates) != 1:
        z,o = 0,0
        for i in candidates:
            if i & base == 0: z += 1
            else: o += 1
        zr = list()
        nzr = list()
        for i in indexvals:
            print("?",i,base)
            flush()
            x = readint()
            if x == 0: zr.append(i)
            else: nzr.append(i)
        if len(zr) != z: # answer & base = 0
            indexvals = zr
            nc = list()
            for c in candidates:
                if c & base == 0: nc.append(c)
            candidates = nc
        else: # answer & base != 0
            indexvals = nzr
            nc = list()
            for c in candidates:
                if c & base != 0: nc.append(c)
            candidates = nc
        base *= 2
    print("!",candidates[0])
    flush()

for _ in range(readint()):
    solve(readint())
