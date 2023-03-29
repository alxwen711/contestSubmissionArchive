import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = input()
    h = [0]*10
    for j in range(4):
        h[int(n[j])] += 1
    a = h.count(1)
    b = h.count(2)
    c = h.count(3)
    d = h.count(4)
    if d == 1: print(-1)
    elif c == 1: print(6)
    else: print(4)
    
