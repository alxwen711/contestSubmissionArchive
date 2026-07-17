import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
0 -> definitely object A
if 1 to n

can we have reverses in this graph?

there must be distinct values?

if x has no duplicates, there is a loop
"""


def solve():
    n = readint()
    ar = readar()
    mi = min(ar)
    ma = max(ar)
    #d = [-1]*(n+1)
    #aindex,bindex = -1,-1
    #for i in range(n):
    #    if d[ar[i]] == -1: d[ar[i]] = i+1
    #    else:
    #        aindex = d[ar[i]]
    #        bindex = i+1
    #        break
    aindex = ar.index(mi)+1
    bindex = ar.index(ma)+1
    print("? "+str(aindex)+" "+str(bindex),flush=True)
    a = readint()
    print("? "+str(bindex)+" "+str(aindex),flush=True)
    b = readint()
    if a != b or (min(a,b) < abs(ma-mi)): return "A"
    #if a == 1 and b == 1: return "A"
    return "B"

for _ in range(readint()):
    print("! "+solve(),flush=True)
    
