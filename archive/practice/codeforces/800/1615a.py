import sys

for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = 0
    for i in range(len(a)):
        b += a[i]
    if b % x == 0: print("0")
    else: print("1")

#finish 8:23, 38 minutes
