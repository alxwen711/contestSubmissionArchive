import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def check(ar,x,n):
    if x == 1:
        for sn in range(n-1):
            if ar[sn] == ar[sn+1]:
                return True
        return False
    h = [2]*x
    for k in range(n):
        h[ar[k]%x] -= 1
    for m in range(x):
        if h[m] > 0: return False
    return True


for i in range(readint()):
    n = readint()
    ar = readar()
    ans = "YES"
    ar.sort()
    for j in range(n//2):
        if check(ar,j+1,n):
            ans = "NO"
            break
    print(ans)
