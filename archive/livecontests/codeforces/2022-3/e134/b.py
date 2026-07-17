import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b,c,d,e = readints()
    top,bot,left,right = False,False,False,False
    if c+e >= a: right = True
    if d+e >= b: bot = True
    if c-e < 2: left = True
    if d-e < 2: top = True
    if (top and bot) or (top and left) or (left and right) or (right and bot): print(-1)
    else: print(a+b-2)
