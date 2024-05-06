import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
only condition is cannot have xR,x+2L
6 2 9 3 1 4 11 5 12 10 7 8
????????????

dp maybe based on choosing L/R?
IF an L AND a R already exist in the setup, literally impossible
if BOTH choices are available at that point, must continue the setup
if only one choice, then possible to *2

why is input 3 160? 128+32?
14/34 WA, it's possible that there can be L AND R with proper forcing
"""

def f(n,ar,s,x):
    br = [1]*n
    p = 0
    for i in range(n):
        v = ar[i]
        choices = br[v] + br[(v+1) % n]
        #print(choices,v)
        if choices == 1: # confirm correct choice is open
            if x == "R" and br[(v+1) % n] == 0: return 0
            if x == "L" and br[v] == 0: return 0
            if s[v] == "?": p += 1
        else: #choices MUST be 2
            if x == "L" and s[v] == "R": return 0
            if x == "R" and s[v] == "L": return 0    
        if x == "L": br[v] = 0
        else: br[(v+1) % n] = 0
        #print(br)
    return pow(2,p,998244353)

n = readint()
ar = readar()
for ii in range(n):
    ar[ii] -= 1
s = sys.stdin.readline()
#l,r = False,False
#if s.count("L") != 0: l = True
#if s.count("R") != 0: r = True
#if l and r: print(0)
#elif l: print(f(n,ar,s,"L"))
#elif r: print(f(n,ar,s,"R"))
#print(f(n,ar,s,"L"))
#print(f(n,ar,s,"R"))
print((f(n,ar,s,"L") + f(n,ar,s,"R")) % 998244353)
