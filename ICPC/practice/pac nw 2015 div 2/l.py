import sys
from math import e,log
#log is already ln, e is e
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,w = readints()
"""
stay or keep going, find max happy value potential, convert to $
can stop, have to determine what is the optimal number of questions to attempt
"""
best = 0.0
p = 1.0
lx = 0.0
check = 0
for i in range(n):
    a,b,c = map(str,input().split())
    b = float(b)
    c = int(c)
    win = b*p*log(1+(c/w))
    loss = p*(1-b)*log(1+(check/w))
    lx += loss
    ev = lx+win
    best = max(best,ev)
    p = p*b
    #print(best)
    if a == "safe": check = c

d = w*(e**best-1)
sys.stdout.write("$")
print("%.2f" % d)
    
