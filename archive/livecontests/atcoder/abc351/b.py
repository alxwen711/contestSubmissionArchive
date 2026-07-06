import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def f(n,ar,br):
    for i in range(n):
        for j in range(n):
            if ar[i][j] != br[i][j]:
                return i+1,j+1

n = readint()
ar = list()
for _ in range(n):
    s = input()
    ar.append(s)
br = list()
for _ in range(n):
    s = input()
    br.append(s)
a,b = f(n,ar,br)
print(a,b)
