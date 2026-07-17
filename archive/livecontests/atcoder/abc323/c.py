import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def calcscore(s,ar):
    score = 0
    for i in range(len(ar)):
        if s[i] == "o": score += ar[i]
    return score

def compute(x,high,s,ar):
    if x == high: return 0
    br = list()
    for j in range(len(ar)):
        if s[j] == "x": br.append(ar[j])
    br.sort()
    br.reverse()

    for k in range(len(br)):
        x += br[k]
        if x > high: return k+1
    
n,m = readints()
ar = readar()
br = list()
high = 0
cr = list()
for i in range(1,n+1):
    s = input()
    br.append(s)
    sc = calcscore(s,ar)+i
    high = max(high,sc)
    cr.append(sc)
    
ans = list()
for j in range(n):
    print(compute(cr[j],high,br[j],ar))
#print(cr)
