import sys
from copy import deepcopy
#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()

"""
do NOT generate all peak numbers

instead, generate ALL sequences going up to 9 digits (17 digit mountains)

there are 73 million such numbers, it's not feasibly possible

there are 4 scenarios:

range below a -> skip, go next

full encapsulate -> get correct back end, full sum

partial encapsulate -> get correct back end, double check ranges

range above b -> return value

[digits+1][whatever first digit is][modulo (dictionary)] = list of all

"""

peaks = [[1,2,3,4,5,6,7,8,9]] # digit fronts
currentlist = [1,2,3,4,5,6,7,8,9]
for _ in range(8):
    newlist = list()
    ar = list()
    for c in currentlist:
        l = c % 10
        for i in range(l,10):
            newlist.append(c*10+i)
            if i != l: ar.append(c*10+i)
    currentlist = newlist
    peaks.append(ar)
    print(len(ar))
print(peaks[1])
print(peaks[8][:5])

backs = list()
for _ in range(9):
    tmp = list()
    for _ in range(10):
        tmp2 = list()
        tmp.append(tmp2)
    backs.append(tmp)
    
for i in range(9):
    for j in range(len(peaks[i])):
        v = int(str(peaks[i][j])[::-1])
        backs[i][peaks[i][j]%10].append(v)
    for k in range(10):
        backs[i][k].sort()
print(backs[2])

# [digits+1][whatever first digit is][modulo (dictionary)] = list of all
def solve(a,b,m): # actual solution goes here
    modar = list()
    for e in range(9):
        tmp = list()
        for f in range(10):
            tmp.append({})
            for g in backs[e][f]:
                r = g % m
                if tmp[f].get(r) == None: tmp[f][r] = list()
                tmp[f][r].append(g)
        modar.append(tmp)
    ans = 0
    for i in range(1,10): # 1 digit cases just in case
        if i >= a and i <= b and i % m == 0: ans += 1

    # now for drunk brute force
    for i in range(1,9):
        for x in peaks[i]: # front
            mincase = x*(10**i)
            maxcase = mincase+(10**i)-1
            if maxcase < a: continue # no added cases here
            elif mincase > b: return ans # everything else is larger
            # at least one possible out
            fullcase = True
            if mincase < a or maxcase > b: fullcase = False
            #print(mincase,maxcase,a,b,fullcase)    
            # compute mod req
            ld = x%10
            r = (mincase-(ld*(10**i))) % m
            #print(x,mincase-(ld*(10**i)))
            target = -r % m
            if modar[i][ld].get(target) != None:
                if fullcase: ans += len(modar[i][ld][target])
                else:
                    for v in modar[i][ld][target]:
                        vv = mincase-(ld*(10**i))+v
                        if vv >= a and vv <= b: ans += 1
    return ans
    


filename = "2a6"
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
