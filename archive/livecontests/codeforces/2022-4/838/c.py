import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

mod = 998244353
for i in range(readint()):
    n = readint()
    s = input()
    v = 1
    ar = [1]*n
    for j in range(1,n):
        if s[j-1] == s[j]:
            v = (v*2) % mod
        else:
            v = 1
        ar[j] = v
    print((sum(ar)) % mod)
