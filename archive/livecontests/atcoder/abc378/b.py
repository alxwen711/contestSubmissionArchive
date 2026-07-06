import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
days = list()
for _ in range(n):
    a,b = readints()
    days.append((a,b))
for _ in range(readint()):
    a,b = readints()
    m,r = days[a-1][0],days[a-1][1]
    print(b+((r-b) % m))
