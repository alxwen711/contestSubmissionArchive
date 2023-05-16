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
    ans = ar[0]
    index = 1
    while ar[index] == ans:
        index += 1
    ans += ar[index]
    print(ans)
