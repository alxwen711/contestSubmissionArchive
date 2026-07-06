import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    ar.sort()
    print(ar[-1]+ar[-2])
