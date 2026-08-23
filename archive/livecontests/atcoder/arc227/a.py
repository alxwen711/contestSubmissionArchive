import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
assign a score to each string

11000011
10100101
10011001

initial submission returns 0 (wrong)

use triangle inequality?

use running average?

median element?
"""

def dist(n,ar,br):
    ans = 0
    for i in range(n):
        ans += abs(ar[i]-br[i])
    return ans

n = readint()
a = readin()
b = readin()
c = readin()


ar = list()
br = list()
cr = list()
#dr = list()

for i in range(2*n):
    if a[i] == "1": ar.append(i)
    if b[i] == "1": br.append(i)
    if c[i] == "1": cr.append(i)
    #if ans[i] == "1": dr.append(i)
    

ans = ["0"]*(2*n)
dr = list()
for i in range(n):
    f = [ar[i],br[i],cr[i]]
    f.sort()
    ans[f[1]] = "1"
    dr.append(f[1])
print(dist(n,dr,ar)+dist(n,dr,br)+dist(n,dr,cr))
print(*ans,sep="")
