import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

ar = list()

for i in range(readint()):
    a,b = map(str,sys.stdin.readline().split())
    ar.append([b,a])
ar.sort()
for j in range(len(ar)):
    print(ar[j][1],ar[j][0])
