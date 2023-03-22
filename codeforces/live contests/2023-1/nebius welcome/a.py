import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b = readints()
    a = abs(a)
    b = abs(b)
    ans = min(a,b)*2
    if a != b: ans += (abs(a-b)*2-1)
    print(ans)
