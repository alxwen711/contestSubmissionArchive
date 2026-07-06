from copy import deepcopy
ar = list()

"""
use 3d dp setup
[number of chairs traversed][number of sections completed][number of chairs in section]
100*50*100 = .5 mill
500 million ops if very badly implemented
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

    """
    tv = 0
    for s in target2:
        tv *= 25
        tv += s
    
    chain = {}
    chain[(0,0)] = 1
    for i in range(len(x)):
        d = {}
        if x[i] == ".": #break chain
            for k in chain.keys():
                kv = k[0]
                if k[1] != 0:
                    kv *= 25
                    kv += k[1]
                if kv <= tv:
                    if d.get((kv,0)) == None: d[(kv,0)] = 0
                    d[(kv,0)] += chain[k]
        elif x[i] == "#":
            for k in chain.keys():
                kv = k[0]
                if d.get((kv,k[1]+1)) == None: d[(kv,k[1]+1)] = 0
                d[(kv,k[1]+1)] += chain[k]
        else:
            for k in chain.keys():
                kv = k[0]
                if k[1] != 0:
                    kv *= 25
                    kv += k[1]
                if kv <= tv:
                    if d.get((kv,0)) == None: d[(kv,0)] = 0
                    d[(kv,0)] += chain[k]
            
            for k in chain.keys():
                kv = k[0]
                if d.get((kv,k[1]+1)) == None: d[(kv,k[1]+1)] = 0
                d[(kv,k[1]+1)] += chain[k]
        chain = d
    #print(v)
    target = list(map(int,v.split(",")))
    tv = 0
    for s in target:
        tv *= 25
        tv += s
    dr = {}
    ans = 0
    for e in chain.keys():
        val = chain[e]
        tt = e[0]
        if e[1] != 0:
            tt *= 25
            tt += e[1]
        if tt == tv: ans += val
    return ans
    """
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
