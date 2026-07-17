import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    a,b,c,d,e,f = readints()
    if a == c == e and (b + d + f) == a: print("YES")
    elif b == d == f and (a+c+e) == b: print("YES")
    elif a == (c+e) and d == f and (b+d) == a: print("YES")
    elif b == (d+f) and c == e and (a+c) == b: print("YES")
    else: print("NO")
