import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
ans = 0
for _ in range(readint()):
    i = sys.stdin.readline()[:-1]
    if i == "Takahashi": ans += 1
print(ans)
