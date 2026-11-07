import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    s = readin()
    if s.count("1") == 1: print(0)
    elif s.count("1") == 2: print(1)
    else:
        ar = list()
        for i in range(n):
            if s[i] == "1": ar.append(i)
        print(ar[-1]-ar[0])
        
