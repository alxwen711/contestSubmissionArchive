import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    v = 1
    ans = list()
    while v <= n:
        ans.append(v)
        v *= 2
    v //= 2
    if v != n:
        diff = n-v
        st = 2**35
        while diff != 0:
            if diff >= st:
                ans.append(ans[-1]+st)
                diff -= st
            st //= 2
    ans.reverse()
    print(len(ans))
    print(*ans)
