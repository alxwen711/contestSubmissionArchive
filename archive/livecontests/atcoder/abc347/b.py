import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
d = {}
n = len(s)
for i in range(n):
    for j in range(n-i):
        d[s[i:i+j+1]] = 1
print(len(list(d.keys())))
