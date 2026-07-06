import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#dummy line for new sub
for i in range(readint()):
    n = readint()
    s = input()
    x = 0
    a = 0
    b = 0
    achain = 0
    bchain = 0
    for j in range(n):
        if s[j] == ">":
            achain += 1
            bchain = 0
        else:
            achain = 0
            bchain += 1
        a = max(a,achain)
        b = max(b,bchain)
    print(max(a,b)+1)
