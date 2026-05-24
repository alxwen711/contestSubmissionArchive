import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
are we sure this is not just frog dp???
probably not due to difference of squares
but ANY positive value can be expressed as the sum of 4 squares
if two squares, there are only so many differences that can be attempted

sqrt(200000) is about 447

Legendre's 3 square thm

4 squares is forced if in form 4**a(8b+7)

precompute every difference and sum with 2 squares, using smallest
squares possible

weird iteration with 3 squares?
from each of the two square totals, then iterate one more time
to get 3 squares
sum and diff would allow everything in 3 squares

if difference is a square, 1
if in the 2-square dict and of minimal distance, 2
some are 3 dist, and some aren't

meet in the middle??

suppose we create the graph (unsure if it's feasible but assume it is)

"""

squares = {}
for i in range(1,448):
    squares[i*i] = 1

sl = list(squares.keys())
sl.sort()

squares2 = {}

for a in range(447,0,-1):
    for b in range(1,a+1):
        diff = a*a-b*b
        squares2[diff] = a # store minimum
    for b in range(1,a+1):
        diff = a*a+b*b
        if diff < 200000: squares2[diff] = a # store minimum
        else: break

squares4 = set()

for b in range(1,25001):
    a = 0
    while (4**a)*(8*b+7) < 200000:
        squares4.add((4**a)*(8*b+7))
        a += 1


anslist = list()
for _ in range(readint()):
    n,q = readints()
    for _ in range(q):
        a,b = readints()
        diff = b-a
        if squares.get(diff) != None: anslist.append("1")
        else:
            minreq = squares2.get(diff,9999999999999)
            if minreq*minreq+a <= n or (b-(minreq*minreq)) >= 1: anslist.append("2")
            elif diff in squares4: anslist.append("4")
            else: anslist.append("3")
            
sys.stdout.write("\n".join(anslist))
