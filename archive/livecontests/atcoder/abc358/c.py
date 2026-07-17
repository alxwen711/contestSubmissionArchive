import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


n,m = readints()
ar = list()
for _ in range(n):
    s = sys.stdin.readline()[:-1]
    x = 0
    for i in s:
        x *= 2
        if i == "o": x += 1
    ar.append(x)

def f(ar,a,target):
    c = 0
    x = 0
    for i in ar:
        if a % 2 == 1:
            x += 1
            c = c | i
        a //= 2
    if c == target: return x
    return -1

target = (2**m)-1
ans = 999
for a in range(2**n):
    v = f(ar,a,target)
    if v != -1: ans = min(ans,v)
print(ans)
