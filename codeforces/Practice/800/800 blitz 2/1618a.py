import sys

for i in range(int(sys.stdin.readline())):
    ar = list(map(int, sys.stdin.readline().split()))
    if ar[0]+ar[1]+ar[2] == ar[6]: print(ar[0],ar[1],ar[2])
    else: print(ar[0],ar[1],ar[3])
