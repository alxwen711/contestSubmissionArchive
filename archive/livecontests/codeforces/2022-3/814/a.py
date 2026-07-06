import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b = readints()
    s = 0
    if a % 2 == 0: s += 1
    if b % 2 == 0: s += 1
    if s == 0: print("Tonya") #no odd
    elif s == 1: print("Burenka") #1 odd
    else: print("Tonya") #2 odd
