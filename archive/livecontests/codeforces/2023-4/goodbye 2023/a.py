import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,k = readints()
    ar = readar()
    x = 1
    for j in ar:
        x *= j
    if 2023 % x == 0:
        print("YES")
        ans = [2023//x]
        while len(ans) != k:
            ans.append(1)
        print(*ans)
    else: print("NO")
