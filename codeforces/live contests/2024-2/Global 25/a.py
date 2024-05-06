import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    s = input()
    ar = list()
    for i in range(n):
        ar.append(int(s[i]))
    if sum(ar) % 2 == 1: print("NO")
    elif sum(ar) == 2:
        ans = "YES"
        index = ar.index(1)
        if index != n-1:
            if ar[index+1] == 1: ans = "NO"
        print(ans)
    else: print("YES")
