import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
readin = lambda: sys.stdin.readline()

"""
easy version has no queries

each query update must be done log n time
when swapping, this can affect at most log n adjacencies
on each row, only track if direct comparison remains valid

(odd lengths will have only childs)

this n,q <= 1000000 thing wants me to do unspeakable acts
"""
def main():

    two = [0,1]
    for _ in range(24):
        two.append(two[-1]*2)


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
 
        if n == 1:
            anslist.append(0)
            for _ in range(q):
                _ = readin()
                anslist.append(0)
            continue

        pushvals = [0]
        tmp1,tmp2 = list(),list()
        while chainsize < n:
            if chainsize == 1:
                tmp1 = ar
                tmp2 = ar
                arlens.append(n)
            else:
                nl = arlens[-1]>>1
                tmp3 = [0]*nl
                tmp4 = [0]*nl
                for i in range(nl):
                    a,b = tmp1[i*2],tmp1[i*2+1]
                    c,d = tmp2[i*2],tmp2[i*2+1]
                    tmp3[i] = a if a < b else b
                    tmp4[i] = c if c > d else d
                if arlens[-1] % 2 == 1:
                    tmp3.append(tmp1[-1])
                    tmp4.append(tmp2[-1])
                tmp1,tmp2 = tmp3,tmp4
                arlens.append(len(tmp1))
            for b in tmp1:
                minlist.append(b)
            for c in tmp2:
                maxlist.append(c)
            pushvals.append(len(minlist))
            # determine comparisons on tmp1 tmp2
            v = len(tmp1)-1
            complist.append(sum([tmp2[j] <= tmp1[j+1] for j in range(v)]))
            targets.append(v)        
            chainsize <<= 1
 
        m = len(complist)
        mask = (1<<m)-1
        for u in range(m):
            if complist[u] == targets[u]: mask ^= two[u+1]
        anslist.append(0 if not mask else two[mask.bit_length()])
 
        # now the hard part of doing the queries

        # redeclare these to be local (look I've been at this problem for a fucking nine or so hours and I don't understand why tf gemini keeps suggesting this but at a certain point i should be afforded the slightest bit of mercy for this utter shitshow of a problem.)
        l_min = minlist
        l_max = maxlist
        l_comp = complist
        l_targ = targets
        l_push = pushvals
        for _ in range(q):
            index,x = readints()
 
            # actual case, first solve initial array
            if index != 0:
                if l_min[index] >= l_max[index-1]: l_comp[0] -= 1
            if index != n-1:
                if l_max[index] <= l_min[index+1]: l_comp[0] -= 1
                    
            # update values and comps
            l_min[index] = x
            l_max[index] = x
        
            if index:
                if l_min[index] >= l_max[index-1]: l_comp[0] += 1
            if index != n-1:
                if l_max[index] <= l_min[index+1]: l_comp[0] += 1

            if l_comp[0] == l_targ[0]: mask &= ~1 
            else: mask |= 1
        
            # now iterate through the remaining sublists
            indent = l_push[0]
            for j in range(1,m):
                redent = indent
                indent = l_push[j]
                index >>= 1 # new updating index
    
                idx = indent+index
                rdx = redent+index*2
                if index:
                    if l_min[idx] >= l_max[idx-1]: l_comp[j] -= 1
                if index != arlens[j]-1:
                    if l_max[idx] <= l_min[idx+1]: l_comp[j] -= 1
                        
                #update values and comps
                if index*2+1 == arlens[j-1]:
                    l_min[idx] = l_min[rdx]
                    l_max[idx] = l_max[rdx]
                else:
                    a,b = l_min[rdx],l_min[rdx+1]
                    c,d = l_max[rdx],l_max[rdx+1]
                    l_min[idx] = a if a < b else b 
                    l_max[idx] = c if c > d else d 

                if index:
                    if l_min[idx] >= l_max[idx-1]: l_comp[j] += 1
                if index != arlens[j]-1:
                    if l_max[idx] <= l_min[idx+1]: l_comp[j] += 1
            
                if l_comp[j] == l_targ[j]: mask &= ~two[j+1]
                else: mask |= two[j+1]
                
            anslist.append(0 if not mask else two[mask.bit_length()])
    #print(*anslist)
    sys.stdout.write(" ".join(map(str,anslist)))

        
main()
