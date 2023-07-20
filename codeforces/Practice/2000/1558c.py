import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
for perumation of length n
operation is to reverse first x elements
x must be odd
2.5n reversals allowed
sum of n is at most 2021, O(n^2) is allowed
odd vals always in odd positions and vice versa
try directly fixing?
pair values as i,i+1, i is each even
find i+1 pos, end if in even pos
if i to left, flip both to front (i+1, i), then full flip, solve n-2 case
if i to right, full reverse then i to left method
3 4 1 2 5 ? solves with 5 3 5 3 5 (34521)
"""

def rev(ar,x): #reverse first x elements
    for i in range(x//2):
        ar[i],ar[x-i-1] = ar[x-i-1],ar[i]

def solve(n,ar):
    c = n
    ans = list()
    while c != 1: #solve last two
        a = c-1 #even
        b = c #odd
        ai = ar.index(a)
        bi = ar.index(b)
        if bi % 2 == 1 or ai % 2 == 0: #odd val on even index or alt
            print(-1)
            return
        if ai + 1 == bi: #left case
            ans.append(bi+1)
            rev(ar,bi+1)
            ans.append(c)
            rev(ar,c)
        elif ai - 1 == bi: #right case
            if bi == 0:
                ans.append(c)
                rev(ar,c)
            else:
                np = c-1-bi
                ans.append(c)
                rev(ar,c)
                ans.append(np+1)
                rev(ar,np+1)
                ans.append(c)
                rev(ar,c)
        else: #5 flips required:
            """
            get b to front (bindex)
            setup b a case (a')
            flip all to get a b case (c)
            flip b a to front (b')
            flip to position (c)
            """
            ans.append(bi+1)
            rev(ar,bi+1)
            if ai < bi: ai = bi-ai
            bi = ai-1
            ans.append(bi+1)
            rev(ar,bi+1)
            np = c-1-bi
            ans.append(c)
            rev(ar,c)
            ans.append(np+1)
            rev(ar,np+1)
            ans.append(c)
            rev(ar,c)
        c -= 2
    print(len(ans))
    print(*ans)

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
