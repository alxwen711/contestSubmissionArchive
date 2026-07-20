import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy version has no queries

each query update must be done log n time
when swapping, this can affect at most log n adjacencies
on each row, only track if direct comparison remains valid

(odd lengths will have only childs)
"""

sanslist = [0,1,2]
for _ in range(30):
    sanslist.append(sanslist[-1]*2)

def findans(complist,targets):
    for i in range(len(complist)):
        if complist[i] == targets[i]:
            return sanslist[i]


fmin = lambda a,b: a if a < b else b
fmax = lambda a,b: a if a > b else b

anslist = list()

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    chainsize = 1
    minlist = list()
    maxlist = list()
    complist = list()
    targets = list()
    arlens = list()
    aa = 0
    while chainsize < n:
        tmp1,tmp2 = list(),list()
        if chainsize == 1:
            tmp1 = ar
            tmp2 = ar
            arlens.append(n)
        else:
            tmp1 = [0]*(arlens[-1]>>1)
            tmp2 = [0]*(arlens[-1]>>1)
            for i in range(arlens[-1]>>1):
                tmp1[i] = fmin(minlist[aa][i*2],minlist[aa][1+i*2])
                tmp2[i] = fmax(maxlist[aa][i*2],maxlist[aa][1+i*2])
            if arlens[-1] % 2 == 1:
                tmp1.append(minlist[aa][-1])
                tmp2.append(maxlist[aa][-1])
            arlens.append(len(tmp1))
            aa += 1
        minlist.append(tmp1)
        maxlist.append(tmp2)
        # determine comparisons on tmp1 tmp2
        v = len(tmp1)-1
        tmp3 = sum([tmp2[j] <= tmp1[j+1] for j in range(v)])
        complist.append(tmp3)
        targets.append(v)        
        chainsize <<= 1

    # flatten minlist and maxlist to 1D
    pushvals = [0]
    milist = list()
    malist = list()
    for a in range(len(minlist)):
        for b in minlist[a]:
            milist.append(b)
        for c in maxlist[a]:
            malist.append(c)
        pushvals.append(len(milist))
    minlist = milist
    maxlist = malist

    # dummy values to ensure a solution is found
    complist.append(0)
    targets.append(0)

    
    anslist.append(findans(complist,targets))

    # now the hard part of doing the queries
    m = len(complist)-1
    for _ in range(q):
        i,x = readints()
        index = i
        if m == 0:
            anslist.append(findans(complist,targets))
            continue

        # actual case, first solve initial array
        if index != 0:
            if ar[index] >= ar[index-1]: complist[0] -= 1
        if index != n-1:
            if ar[index] <= ar[index+1]: complist[0] -= 1

        # update values and comps
        ar[index] = x

        if index != 0:
            if ar[index] >= ar[index-1]: complist[0] += 1
        if index != n-1:
            if ar[index] <= ar[index+1]: complist[0] += 1
        
        # now iterate through the remaining sublists
        for j in range(1,m):
            indent = pushvals[j]
            redent = pushvals[j-1]
            index >>= 1 # new updating index
            if index != 0:
                if minlist[indent+index] >= maxlist[indent+index-1]: complist[j] -= 1
            if index != arlens[j]-1:
                if maxlist[indent+index] <= minlist[indent+index+1]: complist[j] -= 1

            #update values and comps
            #pa,pb = minlist[j][index],maxlist[j][index]
            if index*2+1 == arlens[j-1]:
                minlist[indent+index] = minlist[redent+index*2]
                maxlist[indent+index] = maxlist[redent+index*2]
            else:
                minlist[indent+index] = fmin(minlist[redent+index*2],minlist[redent+index*2+1])
                maxlist[indent+index] = fmax(maxlist[redent+index*2],maxlist[redent+index*2+1])
            
            if index != 0:
                if minlist[indent+index] >= maxlist[indent+index-1]: complist[j] += 1
            if index != arlens[j]-1:
                if maxlist[indent+index] <= minlist[indent+index+1]: complist[j] += 1
            #if pa == minlist[j][index] and pb == maxlist[j][index]: break # remaining will not change
        anslist.append(findans(complist,targets))

sys.stdout.write("\n".join(map(str,anslist)))

        
        
