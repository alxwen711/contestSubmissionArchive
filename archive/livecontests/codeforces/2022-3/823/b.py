import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def bfunc(x,ar,br) -> bool:
    pos = -1
    longest = -1
    for j in range(len(ar)):
        y = (abs(ar[j]-x)+br[j])
        if longest < y:
            pos = ar[j]
            longest = y
    if pos > x: return False
    else: return True
#test original sub
def bsearch(low, high, ar, br):
    for i in range(25):
        mid = (low+high)/2 
        if bfunc(mid,ar,br): high = mid
        else: low = mid
    return (low+high)/2

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(bsearch(min(ar),max(ar),ar,br))
