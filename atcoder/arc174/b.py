import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
get average to at least 3
"""
for _ in range(readint()): 
    ar = readar() # 5 values
    br = readar() # 5 values
    req = ar[0]*2+ar[1]-ar[3]-(2*ar[4]) # extra stars needed
    if req <= 0: print(0) # no bribe needed
    elif req % 2 == 0:
        print(min(br[3]*req,br[4]*req//2))
    else:
        print(min(br[3]*req,br[4]*((req+1)//2),br[4]*(req//2)+br[3]))
