import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x = input()
    y = input()
    h = [0]*26
    h[ord(x[0])-97] += 1
    h[ord(x[1])-97] += 1
    h[ord(y[0])-97] += 1
    h[ord(y[1])-97] += 1
    print(25-h.count(0))
