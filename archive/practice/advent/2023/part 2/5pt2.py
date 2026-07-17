#somehow solves this, good luck understanding this
def lengthen(segments,ar):
    n = len(ar)
    ans = list()
    index = 0
    st = segments[index][0]
    base = segments[index][1]
    ed = base+segments[index][2]
    i = 0
    print("last value tracked:",segments[-1][1]+segments[-1][2])
    while i != n:
        if ed < ar[i][1]: #end before start point, direct map 
            ans.append((st,base,ed-base))
            index += 1
            st = segments[index][0]
            base = segments[index][1]
            ed = base+segments[index][2]
        elif base < ar[i][1]: #bring start point to sync with segment
            dist = ar[i][1]-base-1
            ans.append((st,base,dist))
            st += dist+1
            base = ar[i][1]
        else:
            nmp = ar[i][0]+(base-ar[i][1])
            seged = ar[i][1]+ar[i][2]-1
            if base > seged: #past seg
                i += 1
            elif ed > seged: #contains full seg
                dist = seged-base
                ans.append((st,nmp,dist))
                st += dist+1
                base = seged+1
                i += 1
            else: #new index inc needed
                dist = ed-base
                ans.append((st,nmp,dist))
                index += 1
                if index == len(segments): #something broke
                    print("index problem")
                    print(st,nmp,dist)
                    print(ar[i])
                st = segments[index][0]
                base = segments[index][1]
                ed = base+segments[index][2]
    while index != len(segments):
        ans.append((st,base,ed-base))
        index += 1
        if index == len(segments): break
        st = segments[index][0]
        base = segments[index][1]
        ed = base+segments[index][2]
    #re-sort to new destination points
    ans.sort(key = lambda x: x[1])
    return ans

def calc(l,r,segments):
    ans = 7538946892489067438967439672946784396348962893476
    for i in range(len(segments)):
        bv = segments[i][0]
        ev = bv+segments[i][2]
        if r < bv: break
        elif l <= bv: ans = min(ans,segments[i][1])
        elif l <= ev: ans = min(ans,segments[i][1]+(l-bv))
    return ans

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
print("er:", er)
print("full range up to 20 billion")
#(starting loc,actual loc,length)
segments = [(-1000,-1000,20000001000)]
print(segments)
segments = lengthen(segments,sos)
print("test:")
print(segments)
segments = lengthen(segments,ar)
segments = lengthen(segments,br)
segments = lengthen(segments,cr)
segments = lengthen(segments,dr)
segments = lengthen(segments,er)
segments = lengthen(segments,fr)
segments.sort() #re-re-sort to base segments
print(segments)

ans = 897789879748948910814984765676844686
print("seed calcs")
for i in range(len(seeds)//2):
    st = seeds[2*i]
    ed = st+seeds[2*i+1]-1
    ans = min(ans,calc(st,ed,segments))
print("final:",ans)
