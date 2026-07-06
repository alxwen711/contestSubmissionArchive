import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
h = [0]*26
x = len(s)
for i in range(x):
    h[ord(s[i])-97] += 1
h.sort()
print(x-h[-1]-h[-2])
