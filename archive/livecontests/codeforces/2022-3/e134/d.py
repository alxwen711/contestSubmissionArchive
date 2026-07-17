import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
check if legal, then check if subset
"""

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    a,b = list(),{}
    for j in range(30):
        a.append([0]*n)
        b[j] = 0
    #solve array a
    for k in range(n):
        x = bin(ar[k])[2:]
        #print(x)
        for l in range(len(x)):
            if x[-l-1] == "1": a[l][k] = 1
    #solve array b
    for m in range(n):
        x = bin(br[m])[2:]
        for p in range(len(x)):
            if x[-p-1] == "1": b[p] += 1
    zero = True
    prev = None
    ans = 0
    #print(a)
    for r in range(30):
        if sum(a[-r-1])+b[29-r] == n:
            #possible, but how to check if still possible with previous restrictions?
            """
            assign a to b via keys for each bit
            if bits have overlapping keys, check if enough overlapping keyholes exist
            how to choose the keyholes??
            also n^2 memory is too much
            dictionary setup where the key is a list for a bits leading to list for b bits
            still need to solve cases where two sets share more keyholes than keys without
            using a sudoku setup (n^2 memory)
            could optimize to at most n/2 keys, still 2500mb at minimum
            """
            if zero:
                zero = False
                prev = sum(a[-r-1])
                ans += 2**(29-r)
            elif sum(a[-r-1]) <= prev:
                prev = sum(a[-r-1])
                #ans += 2**(29-r)
                #check if subset?
                
                
                sub = True
                for rr in range(n):
                    if prev[rr] == 0 and a[-r-1][rr] == 1:
                        sub = False
                        break
                if sub:
                    prev = a[-r-1]
                    ans += 2**(29-r)
                
    print(ans)




                
        
