import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()

"""
MAKE SURE YOU TEST TIME LIMIT FIRST
"""

from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    return ar


ref = sieve(10000000)

def solve(n): # actual solution goes here
    ans = 0
    for i in range(2,n+1):
        if ref[i] and ref[i-2]: ans += 1
        if i == 5: ans += 1
    return ans

filename = "1b3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    n = readint()
    ans.append(solve(n))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

