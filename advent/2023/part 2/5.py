#brute force method, enjoy 5 hours of waiting

def ci(x):
    return list(map(int,x.split(" ")))

def floc(x,ar):
    #bin search to speedup
    low = 0
    high = len(ar)-1
    while high - low > 1:
        mid = (low+high)//2
        if ar[mid][1] > x: high = mid
        else: low = mid
    index = high
    if ar[high][1] > x: index = low
    if ar[low][1] > x: return x
        
    i = ar[index]
    l = i[1]
    r = l+i[2]-1
    if l <= x <= r: #istfg if there's overlap
        diff = x-l
        return i[0]+diff
    return x

def getloc(x,sos,ar,br,cr,dr,er,fr):
    p = x
    p = floc(p,sos)
    p = floc(p,ar)
    p = floc(p,br)
    p = floc(p,cr)
    p = floc(p,dr)
    p = floc(p,er)
    p = floc(p,fr)
    return p
    

#input, default to basic integer reading file
f = open("5.txt",'r')
ar = list()
br = list()
cr = list()
dr = list()
er = list()
fr = list()

sos = list()

#get seeds
seeds = f.readline()[:-1]
seeds = seeds.split(":")[1]
seeds = seeds.lstrip()
print(seeds)
seeds = list(map(int,seeds.split(" ")))
f.readline()
f.readline()
#sos
sos.append(ci(f.readline()[:-1]))
sos.append(ci(f.readline()[:-1]))
sos.append(ci(f.readline()[:-1]))
f.readline()

f.readline()
while True:    
    #sof
    l = f.readline()
    if len(l) == 1: break
    ar.append(ci(l[:-1]))

f.readline()
while True:    
    #sof
    l = f.readline()
    if len(l) == 1: break
    br.append(ci(l[:-1]))

f.readline()
while True:    
    #sof
    l = f.readline()
    if len(l) == 1: break
    cr.append(ci(l[:-1]))

f.readline()
while True:    
    #sof
    l = f.readline()
    if len(l) == 1: break
    dr.append(ci(l[:-1]))

f.readline()
while True:    
    #sof
    l = f.readline()
    if len(l) == 1: break
    er.append(ci(l[:-1]))

f.readline()
while True:    
    #sof
    l = f.readline()
    if not l: break
    fr.append(ci(l[:-1]))

f.close()

print(seeds)
print(sos)

ans = 897789879748948910814984765676844686
print(sum(seeds[1::2]))
print(len(seeds))

sos.sort(key = lambda x: x[1])
ar.sort(key = lambda x: x[1])
br.sort(key = lambda x: x[1])
cr.sort(key = lambda x: x[1])
dr.sort(key = lambda x: x[1])
er.sort(key = lambda x: x[1])
fr.sort(key = lambda x: x[1])

print(sos)

print("begin pain")
for i in range(len(seeds)//2):
    print(i,seeds[2*i])
    for j in range(seeds[2*i],seeds[2*i]+seeds[2*i+1]):
        nv = getloc(j,sos,ar,br,cr,dr,er,fr)
        if nv < ans:
            ans = nv
            print("new ans:",ans)
        if j % 1000000 == 0: print(j)
     
print("final:",ans)

