import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
x = 0 count - 1 count
if x == 0: can start either way
x == 1: intentionally start 0 (even count or 0 is up 1)
x == -1: intentionally start 1
anything else: impossible
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    v = 0
    for i in s:
        if i == "0": v += 1
        else: v -= 1
    if abs(v) >= 3: print(-1)
    else:
        a,b = 0,0 # highest with a 0 st, highest with a 1 st
        for i in s:
            if i == "0":
                if a % 2 == 0: a += 1
                if b % 2 == 1: b += 1
            else:
                if a % 2 == 1: a += 1
                if b % 2 == 0: b += 1
        ans = 0
        if v == 0: ans = max(a,b)
        elif v == 1:
            ans = max(a,b - b%2)
        elif v == -1:
            ans = max(a-a%2,b)
        elif v == 2:
            ans = a-((a+1)%2)
        else:
            ans = b-((b+1)%2)
        print(-1 if ans == 0 else n-ans)
        
