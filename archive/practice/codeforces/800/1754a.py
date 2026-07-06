import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    s = input()
    x = 0
    for j in range(n):
        if s[j] == "Q":
            x += 1
        else:
            x = max(x-1,0)
    if x == 0: print("Yes")
    else: print("No")
