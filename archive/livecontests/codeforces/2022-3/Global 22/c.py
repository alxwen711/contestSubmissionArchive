import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    even,odd = 0,0
    for j in range(n):
        if ar[j] % 2 == 0: even += 1
        else: odd += 1
    if odd % 4 == 0 or odd % 4 == 3: print("Alice")
    elif odd % 4 == 2: print("Bob")
    elif even % 2 == 1: print("Alice")
    else: print("Bob")
