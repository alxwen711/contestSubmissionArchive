import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    even = list()
    odd = list()
    for j in range(n):
        if ar[j] % 2 == 1: odd.append([ar[j],j+1])
        else: even.append([ar[j],j+1])
    if len(odd) >= 1 and len(even) >= 2:
        print("YES")
        print(odd[0][1],even[0][1],even[1][1])
    elif len(odd) >= 3:
        print("YES")
        print(odd[0][1],odd[2][1],odd[1][1])
    else: print("NO")
