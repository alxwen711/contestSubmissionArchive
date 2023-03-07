import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
m = 998244353
for i in range(readint()):
    l,r = readints()
    ansa = 0
    x = l
    while x <= r:
        ansa += 1
        x *= 2
    ms = r//(2**(ansa-1))
    three = -1
    if ansa != -1:
        three = r//(2**(ansa-2)*3)
    if three >= l:
        ansb = int((three-l+1)*(ansa-1)+(ms-l+1))
        print(ansa,ansb)
    else:
        ansb = int(ms-l+1)
        print(ansa,ansb)
    
