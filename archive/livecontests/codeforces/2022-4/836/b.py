import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1101
0010
1000
0001

2 -> 1 3
4 -> 1 3 2 2 

"""





for i in range(readint()):
    n = readint()
    ar = list()
    if n % 2 == 1:
        for snth in range(n):
            ar.append(42069)
    else:
        ar.append(1)
        ar.append(3)
        for htnhtn in range(n-2):
            ar.append(2)
    print(*ar)
