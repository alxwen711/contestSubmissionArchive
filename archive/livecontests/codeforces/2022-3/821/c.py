import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
endpoints need same val
e ... o -> copy l
o ... e -> copy l
e ... e ->
o ... o ->
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    print(n-1)
    if n != 1: print(1,n)
    even = True
    if ar[0] % 2 == 1: even = False
    for j in range(n-2):
        if even:
            if ar[j+1] % 2 == 1: print(1,j+2)
            else: print(j+2,n)
        else:
            if ar[j+1] % 2 == 0: print(1,j+2)
            else: print(j+2,n)
    
