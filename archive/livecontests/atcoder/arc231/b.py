import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
find set x and y such that
mex(X) = A -> X must have 0 to A-1 and cannot have A
mex(Y) = B -> Y must have 0 to B-1 and cannot have B
mex(X ^ Y) = C -> taking any xor from X and Y is mex value C

C >= max(A,B) seems correct; if both non-0 trivial. 0 case is provable
C can be lower (5 0 4 is valid)
0 1 2 3 4
1
0 1 2 3

A and B go up to 1000; if we need larger values for C,
we can use 1024+ to construct them (2026 is convinient for the limit)

case where a and b are not 0 is simple as C >= max(A,B) is forced (both have 0)

if both of these are 0,
c = 0 -> single element in a and b, not equal
c = 1,2,3... -> a has 1024, b has 1024,1025,1026...

if only one of these are 0 (assume b)
use the 1024 trick again?

"""

for _ in range(readint()):
    a,b,c = readints()
    if a == 0 or b == 0:
        print("Yes")
        ar = [0]
        br = [0]
        for i in range(a):
            ar.append(i)
            ar[0] += 1
        for j in range(b):
            br.append(j)
            br[0] += 1
        if c == 0:
            ar.append(1024)
            br.append(1025)
            ar[0] += 1
            br[0] += 1
        else:
            ar.append(1024)
            ar[0] += 1
            for k in range(c):
                br.append(k+1024)
                br[0] += 1
        print(*ar)
        print(*br)
    else: # determine what the minimum c must be
        # a and b are relatively small, this could be lightly bruteforced
        alim = 0
        #if a > 10:
        #    alim = 1
        #    while alim*2 < a:
        #        alim *= 2
        blim = 0
        #if b > 10:
        #    blim = 1
        #    while blim*2 < b:
        #        blim *= 2
        h = [0]*1024
        for e in range(alim,a):
            for f in range(blim,b):
                h[e ^ f] = 1
        minc = max(a,b)
        while minc != 1024:
            if h[minc]: minc += 1
            else: break
        if minc > c: print("No")
        else:
            print("Yes")
            ar = [0]
            br = [0]
            for i in range(a):
                ar.append(i)
                ar[0] += 1
            for j in range(b):
                br.append(j)
                br[0] += 1
            ar.append(1024)
            ar[0] += 1
            for g in range(minc,c):
                br[0] += 1
                br.append(g+1024)
            print(*ar)
            print(*br)
