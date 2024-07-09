import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,a = readints()
ar = readar()
st = 0
for i in ar:
    st = max(i,st)
    print(st+a)
    st += a
