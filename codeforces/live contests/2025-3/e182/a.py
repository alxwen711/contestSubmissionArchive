import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for i in range(readint()):
    n = readint()
    ar = readar()
    if sum(ar) % 3 != 0: print(0,0)
    else: # solution exists?
        # just try everything?
        print(1,2)
        #p = [0]
        #for j in ar:
        #    p.append(p[-1]+j)
        #for a in range(1,n-2):
        #    for b in range(a+1,n-1):
        #        if p[a] % 3 == (p[n]-p[b]) % 3
    
    
