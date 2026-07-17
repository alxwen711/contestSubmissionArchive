import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    b,g,x,y,n = readints()
    if (x + y) > n: print(-1)
    else:
        minrooms = (b+g+n-1)//n
        if minrooms*x <= b and minrooms*y <= g: print(minrooms)
        else: print(-1)
