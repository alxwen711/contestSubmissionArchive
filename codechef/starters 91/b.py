import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    od = (n+1)//2 #odd values
    #each set has odd num of odd
    od -= (k-1)
    n -= (2*k-2)
    if n >= 2 and od % 2 == 1: print("YES")
    else: print("NO")
