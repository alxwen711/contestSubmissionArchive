import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    a,b,c,d = 0,0,0,0
    for j in range(n):
        x,y = readints()
        if x > a: a = x
        if x < b: b = x
        if y > c: c = y
        if y < d: d = y
    ans = a+c+abs(b)+abs(d)
    print(ans*2)
