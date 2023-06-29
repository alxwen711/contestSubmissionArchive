import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,x = readints()
    ar = readar()
    br = readar()
    cr = readar()
    ans = 0
    for a in ar:
        if a | x == x: ans = ans | a
        else: break
    for b in br:
        if b | x == x: ans = ans | b
        else: break
    for c in cr:
        if c | x == x: ans = ans | c
        else: break
    if ans == x: print("Yes")
    else: print("No")
