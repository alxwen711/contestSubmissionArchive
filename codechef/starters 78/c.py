import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
co = 2**35



for i in range(readint()):
    n = readint()
    if n != 0:
        a = 1
        b = 2
        c = n+co
        d = co
        print(a,b,c,d)
    else:
        print(2,6,1,3)
