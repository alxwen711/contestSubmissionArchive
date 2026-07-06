import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = sys.stdin.readline()[:-1]
t = sys.stdin.readline()[:-1]
ar = list()
index = 0
for i in s:
    while t[index] != i:
        index += 1
    ar.append(index+1)
    index += 1
print(*ar)
