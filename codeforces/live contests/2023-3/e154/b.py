import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
strings will always start with 0 and end with 1
could be O(n^2)
"""
def solve(n,ar,br):
    for i in range(n-1):
        if ar[i] == 0 and br[i] == 0 and ar[i+1] == 1 and br[i+1] == 1: return "YES"
    return "NO"
    

for i in range(readint()):
    a = sys.stdin.readline()
    b = sys.stdin.readline()
    n = len(a)-1
    ar = list()
    br = list()
    for j in range(n):
        ar.append(int(a[j]))
        br.append(int(b[j]))
    print(solve(n,ar,br))





    
