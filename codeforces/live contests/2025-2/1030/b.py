import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    print(2*n-3)
    for i in range(n):
        if i == 0:
            print(1,2,n)
        elif i == n-1:
            print(n,1,n)
        else:
            print(i+1,1,i+1)
            if i != n-2: print(i+1,i+2,n)
