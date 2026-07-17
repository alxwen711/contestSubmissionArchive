import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
m = 1000000007
for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    ar.sort()
    br.sort()
    ans = 1
    st = n-1
    for j in range(n):
        x = br[-j-1]
        while st != -1:
            if ar[st] > x: st -= 1
            else: break
        v = n-st-1
        ans = (ans*(v-j)) % m
        if ans == 0: break
    print(ans)
