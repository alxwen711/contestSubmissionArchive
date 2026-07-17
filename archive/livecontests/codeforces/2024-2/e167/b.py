import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def f(a,b,i,nb):
    ans = 0
    for c in a:
        if i == nb: break
        if c == b[i]:
            i += 1
            ans += 1
    return ans
for _ in range(readint()):
    a = sys.stdin.readline()[:-1]
    b = sys.stdin.readline()[:-1]
    nb = len(b)
    x = 0
    for i in range(nb):
        x = max(x,f(a,b,i,nb))
    print(len(a)+nb-x)
