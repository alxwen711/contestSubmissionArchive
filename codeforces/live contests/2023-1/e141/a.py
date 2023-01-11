import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    ar.reverse()
    if ar[0] == ar[1]:
        tmp = ar[1]
        ar[1] = ar[-1]
        ar[-1] = tmp
    ans = "YES"
    s = 0
    for j in range(n):
        if ar[j] == s:
            ans = "NO"
            break
        s += ar[j]
    print(ans)
    if ans == "YES": print(*ar)
