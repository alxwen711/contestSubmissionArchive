import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m = readints()
    a = input()
    b = input()
    if n == m:
        if a == b: print("YES")
        else: print("NO")
    elif m == 1:
        if a.count(b) == 0: print("NO")
        else: print("YES")
    else:
        bb = len(b)
        if a[-bb:] == b: print("YES")
        elif a[-bb+1:] == b[1:]:
            if a[:len(a)-bb].count(b[0]) == 0: print("NO")
            else: print("YES")

        else: print("NO")
    

