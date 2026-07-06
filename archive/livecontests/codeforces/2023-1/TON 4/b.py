import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n):
    if n % 2 == 0:
        print(-1)
        return
    s = str(bin(n))[2:]
    ar = list()
    for i in range(len(s)-1):
        if s[i] == "1": ar.append(2)
        else: ar.append(1)
    print(len(ar))
    print(*ar)

for i in range(readint()):
    n = readint()
    solve(n)
