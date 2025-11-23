import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


def f(n,ar,i):
    x = i
    ans = 0
    while x != 0:
        if ar[ans % n] == "A":
            x -= 1
        else:
            x //= 2
        ans += 1
    return ans

for _ in range(readint()):
    n,q = readints()
    s = readin()
    ar = readar()
    if s.count("A") == n:
        for i in ar:
            print(i)
    else:
        for i in ar:
            print(f(n,s,i))
