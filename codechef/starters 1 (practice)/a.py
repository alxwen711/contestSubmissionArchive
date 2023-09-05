import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    d,c = readints()
    v = 0
    a0,a1,a2 = readints()
    b0,b1,b2 = readints()
    if a0+a1+a2 >= 150: v += d
    if b0+b1+b2 >= 150: v += d
    if v > c: print("YES")
    else: print("NO")
    
