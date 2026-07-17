import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
for i in range(readint()):
    a,b,c = readints()
    print(max(0,max(b,c)-a+1),max(0,max(c,a)-b+1),max(0,max(b,a)-c+1))

