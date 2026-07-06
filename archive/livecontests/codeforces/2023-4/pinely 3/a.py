import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    a,b,c,d = True,True,True,True
    for _ in range(n):
        x,y = readints()
        if x > 0: a = False
        if x < 0: b = False
        if y > 0: c = False
        if y < 0: d = False
    if a or b or c or d: print("YES")
    else: print("NO")
