import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# +1 wrong for 10 min pen
for i in range(readint()):
    n = readint()
    ar = readar()
    if ar[0] == 1: print("Bob")
    elif ar.count(max(ar)) == n: print("Bob")
    elif ar[0] == min(ar): print("Bob")
    else: print("Alice")
