import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
these are the indices of the values
assign highest values for the 1 indices
assign lowest values for the 2 indices
next highest go to 3, next lowest go to 4
generally assign odd indices high to low and even indices low to high
if the last x non filled spots are removed here, reverse order


"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    miter = max(ar)
    vals = list()
    for _ in range(miter+1):
        tmp = list()
        vals.append(tmp)
    for i in range(n):
        if ar[i] == -1: vals[0].append(i+1)
        else: vals[ar[i]].append(i+1)
    #print(vals)
    ans = [0]*n
    v = 1
    for a in range(2,len(vals),2):
        if vals[a][-1] == n: # order reversal
            #for c in range(1,len(vals[a])):
            #    if vals[a][-c-1] == n-c:
            #        vals[a][-c-1],vals[a][-c] = vals[a][-c],vals[a][-c-1]
            #    else: break
            for c in range(1,len(vals[a])+1): # if runtime, it's probably here
                if c == len(vals[a]):
                    for e in range(c//2):
                        vals[a][-e-1],vals[a][-c+e] = vals[a][-c+e],vals[a][-e-1]
                    break
                if vals[a][-c-1] != n-c:
                    for e in range(c//2):
                        vals[a][-e-1],vals[a][-c+e] = vals[a][-c+e],vals[a][-e-1]
                    break
        for b in vals[a]:
            ans[b-1] = v
            v += 1
    ans[vals[0][0]-1] = v
    v += 1
    sv = len(vals)-1
    if sv % 2 == 0: sv -= 1
    for a in range(sv,0,-2):
        if vals[a][-1] == n: # order reversal
            for c in range(1,len(vals[a])+1): # if runtime, it's probably here
                if c == len(vals[a]):
                    for e in range(c//2):
                        vals[a][-e-1],vals[a][-c+e] = vals[a][-c+e],vals[a][-e-1]
                    break
                if vals[a][-c-1] != n-c:
                    for e in range(c//2):
                        vals[a][-e-1],vals[a][-c+e] = vals[a][-c+e],vals[a][-e-1]
                    break
                
        vals[a].reverse()
        for b in vals[a]:
            ans[b-1] = v
            v += 1
    #print(vals)
    print(*ans)
