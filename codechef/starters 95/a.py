import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = list(map(str,sys.stdin.readline().split()))
    a,b,ab,o = 0,0,0,0
    for j in ar:
        if j == "A": a += 1
        elif j == "B": b += 1
        elif j == "AB": ab += 1
        else: o += 1
    print(o+ab+max(a,b))
