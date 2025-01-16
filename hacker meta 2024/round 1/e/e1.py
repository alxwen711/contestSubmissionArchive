import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()

"""
question is more like how many collisions are there?
is it possible to construct the trie literally?
(probably not, A??K AEWCC in that order screws up, then ACR?S)
"""


def solve(n,ar): # actual solution goes here
    m = 998244353

filename = "1e1"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    n = readint()
    ar = list()
    for _ in range(n):
        ar.append(readin())
    ans.append(solve(n,ar))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

