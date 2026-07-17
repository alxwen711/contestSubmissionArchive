import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m,d = readints()
    ar = readar()
    c = m
    for j in range(m-1):
        c += (ar[j+1]-ar[j]-1)//d
    #st/ed points
    c += max(0,(ar[0]-2)//d)
    c += max(0,(n-ar[-1])//d)
    if ar[0] != 1: c += 1 #total number of cookies
    #print(c,"cookies at base")
    best = c
    freq = 0
    #remove all mid cases
    for k in range(1,m-1):
        #remove ar[k]
        a,b,cc = ar[k-1],ar[k],ar[k+1]
        nc = c-1-((b-a-1)//d)-((cc-b-1)//d)+((cc-a-1)//d)
        #print(nc,k)
        if nc == best: freq += 1
        elif nc < best:
            best = nc
            freq = 1
    #remove front
    nc = c
    if ar[0] != 1:
        a,b = ar[0],ar[1]
        nc = c-1-((a-2)//d)-((b-a-1)//d)+((b-2)//d)
    #print(nc,"st")
    if nc == best: freq += 1
    elif nc < best:
        best = nc
        freq = 1
        
    #remove back
    nc = c-1
    nc -= ((ar[-1]-ar[-2]-1)//d)
    nc -= ((n-ar[-1])//d)
    nc += ((n-ar[-2])//d)
    #print(nc,"ed")
    if nc == best: freq += 1
    elif nc < best:
        best = nc
        freq = 1
    print(best,freq)
    
