import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#each row/col MUST have an odd number of odd vals

def even(n):
    """
    n*n tiles (even number) with even num of odd vals
    """
    ar = list()
    for _ in range(n):
        tmp = [0]*n
        ar.append(tmp)
    if n % 4 == 2: #easy checkerboard
        e = 1
        o = 2
        for i in range(n):
            for j in range(n):
                if (i+j) % 2 == 0:
                    ar[i][j] = e
                    e += 2
                else:
                    ar[i][j] = o
                    o += 2
    else: #need some sort of displacement setup
        #fill entire bottom right corner with odds
        o = 1
        even = 2
        for a in range(n//2,n):
            for b in range(n//2,n):
                ar[a][b] = o
                o += 2
        #single diagonal fill not top left corners
        for c in range(n//2):
            ar[c][n//2+c] = o
            o += 2
            ar[n//2+c][c] = o
            o += 2
        #multi diagonal fill top left corner
        dc = ((n*n)//4-n)//(n//2) #num of diagonals
        for d in range(dc):
            for e in range(n//2):
                ar[e][(d+e) % (n//2)] = o
                o += 2
        #any 0's in the array should be even
        for f in range(n):
            for g in range(n):
                if ar[f][g] == 0:
                    ar[f][g] = even
                    even += 2
                
    for x in ar:
        print(*x)

def odd(n):
    #rip out of time
    ar = list()
    for _ in range(n):
        tmp = [0]*n
        ar.append(tmp)
    odd = 1
    even = 2
    #draw cross
    for c in range(n):
        ar[c][n//2] = odd
        odd += 2
    for d in range(n):
        if d != n//2:
            ar[n//2][d] = odd
            odd += 2
    r = (((n*n)//2+1)-n-n+1)//4
    for a in range(n//2):
        for b in range(n//2):
            if r == 0: break
            ar[a][b] = odd
            odd += 2
            ar[a][b+n//2+1] = odd
            odd += 2
            ar[a+n//2+1][b] = odd
            odd += 2
            ar[a+n//2+1][b+n//2+1] = odd
            odd += 2
            r -= 1
        if r == 0: break
    for e in range(n):
        for f in range(n):
            if ar[e][f] == 0:
                ar[e][f] = even
                even += 2
    for x in ar:
        print(*x)
        

for _ in range(readint()):
    n = readint()
    if n % 2 == 0: even(n)
    else: odd(n)
