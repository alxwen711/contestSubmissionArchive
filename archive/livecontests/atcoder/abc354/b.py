import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
names = list()
ans = 0
for _ in range(n):
    s,c = map(str,sys.stdin.readline().split())
    c = int(c)
    names.append(s)
    ans += c
names.sort()
print(names[ans % n])
