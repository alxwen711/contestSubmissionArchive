import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()


def solve(n,ar): # compute seconds per mile then invert
    l = ar[0][0]
    h = ar[0][1]
    for i in range(1,n):
        nl = ar[i][0]/(i+1)
        nh = ar[i][1]/(i+1)
        if nl > h: return -1
        if nh < l: return -1
        l = max(l,nl)
        h = min(h,nh)
    return 1/h
filename = "1a3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    n = readint()
    ar = list()
    for j in range(n):
        a,b = readints()
        ar.append((a,b))
    ans.append(solve(n,ar))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

