import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n rows
m columns
x and y are array lengths, can be anything from 1 to n+m
naively can choose n from ar, m-1 from br or n-1 from ar, m from br

if 1 row and many columns
19 18 17 16
1 2

18/17/16 in this case are not insertable at all

if only one value has it, try to use
if both have it, add to a counter, wait until it is capped
"""

def solve(ar,br,a,b):
    ans = 0
    extra = 0
    ap,bp = 0,0
    na,nb = len(ar),len(br)
    while a + b != extra:
        if ap == na and bp == nb: return ans
        if ap == na:
            if b != 0:
                b -= 1
                ans += br[bp]
            bp += 1
        elif bp == nb:
            if a != 0:
                a -= 1
                ans += ar[ap]
            ap += 1
        else:
            if ar[ap] > br[bp]:
                if a != 0:
                    a -= 1
                    ans += ar[ap]
                ap += 1
            elif br[bp] > ar[ap]:
                if b != 0:
                    b -= 1
                    ans += br[bp]
                bp += 1
            else: # either one can input it
                extra += 1
                ans += ar[ap]
                ap += 1
                bp += 1
    return ans


            
for _ in range(readint()):
    n,m,x,y = readints()
    ar = readar()
    br = readar()
    ar.reverse()
    br.reverse()
    print(max(solve(ar,br,n,m-1),solve(ar,br,n-1,m)))
