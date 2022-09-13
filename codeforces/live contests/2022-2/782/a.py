import sys
from math import ceil
for i in range(int(sys.stdin.readline())):
    n,r,b = map(int,sys.stdin.readline().split())
    c = ceil(r/(b+1))
    ans = ""
    #b+1 groups of r, max size is c
    hg = r - (c-1)*(b+1)
    lg = (b+1)-hg
    #print(hg,lg)
    for j in range(hg):
        ans += "R"*c+"B"
    for k in range(lg):
        ans += "R"*(c-1)+"B"
    print(ans[:len(ans)-1])
    
