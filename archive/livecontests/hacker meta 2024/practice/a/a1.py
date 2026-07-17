import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,k,ar): # actual solution goes here
    t = min(ar)*(max(1,n*2-3))
    return "YES" if t <= k else "NO"

filename = "pa3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    n,k = readints()
    ar = list()
    for j in range(n):
        br = readar()
        ar.append(br[0])
    ans.append(solve(n,k,ar))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

