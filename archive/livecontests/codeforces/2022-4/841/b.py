import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    a = (n-1)*n*(n+1)*2
    b = (n*(n+1)*(2*n+1))
    c = (a+b)//6
    d = 2022*c
    print(d%1000000007)
    
