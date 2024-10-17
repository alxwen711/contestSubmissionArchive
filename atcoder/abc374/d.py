import sys
from itertools import permutations
from math import sqrt
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# brute force with 6 lines

n,s,t = readints()
lines = list()
ar = list()

def f(n,s,t,lines,p):
    ans = 9999999999999999999999999
    dist1,dist2 = 0,0
    for i in range(2**n): # for all possible endpoints
        g = i
        x,y = 0,0
        d = 0
        for index in p:
            if g % 2 == 0: # ab to cd
                dist1 = sqrt(abs(lines[index][0]-x)**2+abs(lines[index][1]-y)**2)
                dist2 = sqrt(abs(lines[index][0]-lines[index][2])**2+abs(lines[index][1]-lines[index][3])**2)
                x,y = lines[index][2],lines[index][3]
            else:
                dist1 = sqrt(abs(lines[index][2]-x)**2+abs(lines[index][3]-y)**2)
                dist2 = sqrt(abs(lines[index][0]-lines[index][2])**2+abs(lines[index][1]-lines[index][3])**2)
                x,y = lines[index][0],lines[index][1]
            d += dist1/s
            d += dist2/t
            g //= 2
        ans = min(ans,d)
    return ans
            
    


for i in range(n):
    a,b,c,d = readints()
    lines.append((a,b,c,d))
    ar.append(i)
ans = 9999999999999999999999999999
for p in permutations(ar):
    ans = min(ans,f(n,s,t,lines,p))
print(ans)
