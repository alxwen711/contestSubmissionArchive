import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()

"""
up to 640000 squares
can do cross validation within each row/col, how to extend to 2d?

Group all same with each other, then need to eliminate

K part can be done if an array tracking # of possible jumps of length
1,2,...,max(r,c)-1 is being tracked

LT binary, check if there are k jumps of at least distance x

then each spot has several square "rings" to consider
count how many spots on the rings are different (uses some sort of bin table)
then divide by 2 to get the total result for number of jumps of distance x

true LT binary would need to be a sort of 2d sparse tree setup

(this is the point when I see there is 4 minutes left and no hope of
even getting close to implementing this that fast, so rest in pepperoni)
"""
def solve(r,c,k,ar): # actual solution goes here
    

    
filename = "2c1"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    r,c,k = readints()
    ar = list()
    for j in range(r):
        br = readar()
        ar.append(br)
    ans.append(solve(r,ck,ar))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

