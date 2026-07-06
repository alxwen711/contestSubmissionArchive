import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    ar = readar()
    if ar[0] != ar[-1]:
        print("YES")
        print("R"+"B"+"R"*(n-2))
    else:
        print("NO")
