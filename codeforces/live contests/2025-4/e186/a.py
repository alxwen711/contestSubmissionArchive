import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    s = readin()
    ar = list()
    for i in s:
        ar.append(int(i))
    ans = 0
    flag = False
    # first change any 2025->2026
    for j in range(n-3):
        if ar[j] == 2 and ar[j+1] == 0 and ar[j+2] == 2 and ar[j+3] == 5:
            ans = 1
        if ar[j] == 2 and ar[j+1] == 0 and ar[j+2] == 2 and ar[j+3] == 6:
            ans = 0
            break
    print(ans)
