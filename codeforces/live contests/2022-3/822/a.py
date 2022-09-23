import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def f(a,b,c):
    return min(abs(b-a)+abs(c-a),abs(a-b)+abs(c-b),abs(b-c)+abs(a-c))

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    ans = 9873986739863489
    for j in range(n-2):
        ans = min(ans,f(ar[j],ar[j+1],ar[j+2]))
    print(ans)
