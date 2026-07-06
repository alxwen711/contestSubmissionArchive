import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ans = ""
for i in range(n):
    if i % 3 == 2: ans += "x"
    else: ans += "o"
print(ans)
