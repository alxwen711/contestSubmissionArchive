import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def recycle(a):
    x = a
    ans = 0
    while x != 0:
        ans += (x%10)**2
        x //= 10
    return ans

def tune(a,b):
    x,y = a,b
    for _ in range(15):
        x = recycle(x)
        y = recycle(y)
        if x == y: return True
    return False

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if tune(ar[i],ar[j]): ans += 1
    print(ans)
