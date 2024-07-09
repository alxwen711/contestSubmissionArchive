from copy import deepcopy
ar = list()

def ff(ar):
    br = list()
    cr = deepcopy(ar)
    br.append(cr)
    length = len(cr)
    for e in range(length,1,-1):
        tmp = list()
        for f in range(e-1):
            tmp.append(br[-1][f+1]-br[-1][f])
        br.append(tmp)
        if tmp.count(0) == len(tmp): break
    br[-1].append(0)
    for g in range(len(br)-1): #second last, 3rd last, 4th last
        br[-g-2].append(br[-g-2][-1]+br[-g-1][-1])
    return br[0][-1]
#input, default to basic integer reading file
f = open("9.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        br = list(map(int,l.split(" ")))
        br.reverse()
        ar.append(br)
    
f.close()

print(ar[0])
ans = 0
for i in ar:
    ans += ff(i)
print(ans)
