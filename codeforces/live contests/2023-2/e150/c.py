import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
not just change first possible to E
DDDDDDDDDDDE -> -1000
EDDDDDDDDDDE -> 10000
DDDDDDDDDDDD -> 12000

possible moves are either:
change first non-E to an E, will always have no neg dec
dropping letter downwards (careful with ABACCEDDCACE -> ABACCCDDCACE)
change last E to a D
change last D/E to a C
change last C/D/E to a B
change last B/C/D/E to a A

calculating value: find last E, last D, last C, last B
if greater val digit remains, neg, else pos
"""
vals = {"A":1,"B":10,"C":100,"D":1000,"E":10000}

def calc(n,s):
    #print(s)
    l = [-1]*5
    for i in range(n):
        x = ord(s[i])-65
        l[x] = i
    b = -1
    limit = [-1]*5
    for j in range(5):
        b = max(b,l[-j-1])
        limit[4-j] = b
    limit.append(-1) # E is auto pass
    #print(limit)
    ans = 0
    for k in range(n):
        x = s[k]
        v = vals[x]
        index = ord(x)-65
        if k > limit[index+1]: ans += v #check if ties are possible
        else: ans -= v
    #print(s,ans)
    return ans,limit
    

def solve(s):
    n = len(s)
    best,ar = calc(n,s)
    ini = best
    for i in range(1,5):
        if ar[i] != -1:
            x = ar[i]
            ns = s[:x]+chr(i+64)+s[x+1:]
            h,dummy = calc(n,ns)
            best = max(best,h)
    cr = [-1]*5
    for snth in range(n):
        x = ord(s[snth])-65
        if cr[x] == -1: cr[x] = snth
    #print(cr)
    for j in range(4):
        if cr[j] != -1:
            ns = s[:cr[j]]+"E"+s[cr[j]+1:]
            h,dummy = calc(n,ns)
            best = max(best,h)
    return best
        

for i in range(readint()):
    s = input()
    print(solve(s))
