import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b,c = readints()
    x = a-1
    y = abs(b-c)+c-1
    if x > y: print(2)
    elif y > x: print(1)
    else: print(3)
