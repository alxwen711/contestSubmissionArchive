import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()



# generate ALL peak numbers
peaks = [1,2,3,4,5,6,7,8,9,121,232,343,454,565,676,787,898
         ,12321,23432,34543,45654,56765,67876,78987,1234321,2345432,3456543,4567654,
         5678765,6789876,123454321,234565432,345676543,456787654
         ,567898765,12345654321,23456765432,34567876543,45678987654,
         1234567654321,2345678765432,3456789876543,123456787654321
         ,234567898765432,12345678987654321]

for i in peaks:
    s = str(i)
    assert s == s[::-1] and len(s) % 2 == 1

def solve(a,b,m): # actual solution goes here
    ans = 0
    for p in peaks:
        if p >= a and p <= b and p % m == 0: ans += 1
    return ans
    


filename = "2a3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
ans = list()
for i in range(casecount):
    # get input here
    a,b,m = readints()
    ans.append(solve(a,b,m))
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k]))
    f.write("\n")
f.close()

