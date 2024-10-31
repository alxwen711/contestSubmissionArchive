ar = list()
br = list()
"""
wrong answers:
29266
37618

screw it brute force can work
"""
def hor(ar,x,n,m):
    l = x-1
    r = x
    while l >= 0 and r < n:
        if ar[l] != ar[r]: return False
        r += 1
        l -= 1
    return True

def ver(ar,x,n,m):
    l = x-1
    r = x
    while l >= 0 and r < m:
        for snth in range(n):
            if ar[snth][l] != ar[snth][r]: return False
        r += 1
        l -= 1
    return True

def fun(ar,miss):
    n,m = len(ar),len(ar[0])
    #hor line
    ans = 0
    for i in range(1,n):
        if hor(ar,i,n,m) and (100*i) != miss:
            return (100*i)
    #vert line
    for j in range(1,m):
        if ver(ar,j,n,m) and j != miss:
            return j
    #if ans == 0: print("no reflect found")
    return ans

def swap(s):
    if s == ".": return "#"
    return "."

def fun2(ar):
    br = list()
    for i in ar:
        tmp = list()
        for j in range(len(i)):
            tmp.append(i[j])
        br.append(tmp)
    miss = fun(br,9989899878979)
    for a in range(len(br)):
        for b in range(len(br[a])):
            br[a][b] = swap(br[a][b])
            xx = fun(br,miss)
            if xx != 0 and xx != miss: return xx
            br[a][b] = swap(br[a][b])
    print(br,"crash")
    return "potato"

#input, default to basic integer reading file
f = open("13.txt",'r') 
while True:
    l = f.readline()
    if not l: break
    if l[0] == "f": break
    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    else:
        br.append(ar)
        ar = list()
    
f.close()
#print(br[0])
print(len(br))
count = 0
ans = 0
for i in br:
    #print(i)
    #if fun(i) == 0: print(i)
    ans += fun2(i)
    count += 1
    print(count,"done")
    
print(ans)
print(br[-1])
