import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# just make it all negative

for _ in range(readint()):
    n = readint()
    ar = readar()
    pos = True
    ans = list()
    for i in range(n-1,-1,-1):
        if pos:
            if ar[i] > 0:
                pos = False
                ans.append(i+1)
        else:
            if ar[i] < 0:
                pos = True
                ans.append(i+1)
    print(len(ans))
    print(*ans)
