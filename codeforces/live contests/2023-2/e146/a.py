import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b = readints()
    diff = a-b
    if a % 2 == 0: print("YES")
    elif diff % 2 == 0 and diff >= 0: print("YES")
    else:
        diff -= b
        if diff % 2 == 0 and diff >= 0: print("YES")
        else: print("NO")
