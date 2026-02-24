import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# some modulo of 3 is needed

for _ in range(readint()):
    x,y = readints()
    if (x+y) % 3 == 0:
        mc = (x+y)//3
        if 2*mc <= x <= 4*mc: print("YES")
        else: print("NO")
    else: print("NO")
