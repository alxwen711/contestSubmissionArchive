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
    if n % 2 == 0:
        ar = list()
        for i in range(n//2):
            ar.append(2*i+2)
            ar.append(2*i+1)
        print(*ar)
    else:
        ar = [i+1 for i in range(n)]
        ar.reverse()
        print(*ar)
            
