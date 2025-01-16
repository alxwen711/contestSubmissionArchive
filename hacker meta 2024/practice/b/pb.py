import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()


def solve(n,k): # actual solution goes here
    p = k*100000000
    low = 0
    high = 10000000000-p
    target = p**(n-1)*10000000000
    while high-low > 1:
        mid = (low+high)//2
        if (p+mid)**(n) < target: low = mid
        else: high = mid
    return low/100000000

filename = "pb3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    n,k = readints()
    ans.append(solve(n,k))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

