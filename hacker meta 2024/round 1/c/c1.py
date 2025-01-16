import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()


"""
can be reconstructed into two values: number of spots left/right

5
201 200 1
185 183 2
250 180 0
77665544332211 11223344556677 0
83716485936440 64528193749358 1938563682

l = 1, r = 1 -> 3
l = 2, r = 2 -> 10
l = 70, r = 0 -> 70

r factor is a bit misleading, this is really how much within lowest
you've ever been you are allowed to be

+1/-1 is 50/50

l and r are practically infinite

if you go down 1 from best, then reset to 0

otherwise, there is some sort of cluster setup
r = 0 -> 1 day set
r = 1 -> 3 day set
r = 2 -> 5 day set
r = 3 -> 7? day set
1/2, 0, 1/4, 0, 1/8, 0, 1/16
1/2, 0, 1/8, 0, 3/32, 0, 9/128
"""

def solve(w,g,l): # actual solution goes here
    m = 998244353
    left = w-g
    right = l
    return (left*(right*2+1)) % m
    
filename = "1c3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    w,g,l = readints()
    ans.append(solve(w,g,l))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

