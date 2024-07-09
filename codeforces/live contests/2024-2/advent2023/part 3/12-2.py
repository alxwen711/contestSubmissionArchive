ar = list()

"""
use 3d dp setup
[number of chairs traversed][number of sections completed][number of chairs in section]
100*50*100 = .5 mill
500 million ops if very badly implemented

solutions are either all sections done
OR all except last is done, and last has correct number done (no . to end)

chain break?
all 0 chains stay 0 chains
all 1+ chains must be in correct position to move to completed segment
otherwise, full delete
"""

def function(xr):
    #print(xr)
    x,v = xr.split(" ")
    x = x+"?"+x+"?"+x+"?"+x+"?"+x
    target = list(map(int,v.split(",")))
    target2 = list()
    for _ in range(5):
        for ss in target:
            target2.append(ss)
    target = target2
    
    dp = list()
    for _ in range(len(x)+1):
        tmp2 = list()
        for _ in range(len(target)+1):
            tmp = [0]*(len(x)+1)
            tmp2.append(tmp)
        dp.append(tmp2)
    dp[0][0][0] = 1

    for i in range(len(x)):
        if x[i] == "?" or x[i] == ".": #chain break
            for c in range(len(target)+1):
                dp[i+1][c][0] += dp[i][c][0]
            for d in range(len(target)):
                dp[i+1][d+1][0] += dp[i][d][target[d]]
        if x[i] == "?" or x[i] == "#": #chain add
            for a in range(len(target)+1):
                for b in range(1,len(x)+1):
                    dp[i+1][a][b] += dp[i][a][b-1]
    return dp[len(x)][len(target)][0]+dp[len(x)][len(target)-1][target[-1]]
        

#input, default to basic integer reading file
f = open("12.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

ans = 0
print(len(ar))
count = 0
for x in ar:
    x = x.rstrip()
    ans += function(x)
    count += 1
    print(count,"done")
print(ans)
