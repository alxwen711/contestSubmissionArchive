import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    a,b = readints()
    a *= 9
    b *= 10
    if a == b: print("EITHER")
    elif a < b: print("ONLINE")
    else: print("DINING")
