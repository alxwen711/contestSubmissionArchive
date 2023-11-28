import sys
from math import lcm
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
only need to consider at most the 3 closest

"""
#2 val problem
def doub(n,vals,a,br):
    #print(a,br)
    lowa,ai = 3474768934769437697689234907927940173974901,-1
    lowb,bi = 8790430783983983437403787394810978134948319,-1
    for i in range(n):
        x = (-vals[i]) % a
        if x < lowa:
            lowb,bi = lowa,ai
            lowa,ai = x,i
        elif x < lowb:
            lowb,bi = x,i
    dr = [(lowa,ai),(lowb,bi)]
    #print(dr,br)
    ans = 4857024854802795347098753408954879230342546567786365452567
    for aa in range(2):
        for bb in range(2):
            if dr[aa][1] != br[bb][1]:
                ans = min(ans,dr[aa][0]+br[bb][0])
    return ans
        

n,a,b,c = readints()
vals = readar()
ar = list()
br = list()
cr = list()
for i in range(n): #if it's really bad then remove these sorts (probably not the answer)
    x = vals[i]
    ar.append(((-x) % a,i))
    br.append(((-x) % b,i))
    cr.append(((-x) % c,i))
ar.sort()
br.sort()
cr.sort()
# singular tests first
trip = lcm(a,b,c)
ans = 87465766594946547589426795647359436579843562974563978457694679587393
for j in range(n):
    ans = min(ans, (-vals[j]) % trip)

#print(ans)

#double tests
if n > 1:
    ans = min(ans,doub(n,vals,lcm(a,b),cr))
    ans = min(ans,doub(n,vals,lcm(a,c),br))
    ans = min(ans,doub(n,vals,lcm(c,b),ar))

#print(ans)

#triple tests
if n > 2:
    #try all 27 combinations
    for aa in range(3):
        for bb in range(3):
            for cc in range(3):
                if (ar[aa][1] != br[bb][1]) and (br[bb][1] != cr[cc][1]) and (ar[aa][1] != cr[cc][1]):
                    ans = min(ans,ar[aa][0]+br[bb][0]+cr[cc][0])                    
print(ans)
