import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# how many are on the diagonals
for _ in range(readint()):
    n,s = readints()
    ans = 0
    for _ in range(n):
        a,b,c,d = readints()
        if (c == d and a == b) or (c+d == s and a != b): ans += 1
    print(ans)
