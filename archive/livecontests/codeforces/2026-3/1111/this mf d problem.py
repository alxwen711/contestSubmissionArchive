import sys
from io import StringIO

#input functions
readin = lambda: sys.stdin.buffer.readline()
readint = lambda: int(readin())
readints = lambda: map(int,readin().split())
readar = lambda: list(map(int,readin().split()))


"""
easy version has no queries

each query update must be done log n time
when swapping, this can affect at most log n adjacencies
on each row, only track if direct comparison remains valid

(odd lengths will have only childs)

this n,q <= 1000000 thing wants me to do unspeakable acts

literally the same submission as 383416420, see if this goes TLE on 15

okay so this probably needs to be a 1d binary seg tree to make
the parent/child locating much faster

the problem is forcing me to treat +18 and ^1 type operations as different.
this is actually the most fuck you constraints of all time

OKAY I GUESS WE ARE INDEXING FROM 1 NOW.
"""

    


def main():

    two = [1]
    for _ in range(23):
        two.append(two[-1]<<1)
    endme = StringIO()

    for _ in range(readint()):
        n,q = readints()
        ar = readar()

        if n == 1: # trivial edge case
            endme.write("0 ")
            for _ in range(q):
                _ = readin()
                endme.write("0 ")
            continue

        # construct the tree
        chainsize = 1
        for snth in two:
            if snth >= n:
                chainsize = snth
                break

        intscore = 2**30
        for _ in range(chainsize-n):
            ar.append(intscore) # these will always be sorted

        minlist = [intscore]*(chainsize)+ar
        maxlist = [0]*(chainsize)+ar


        n = chainsize
        
        #for aa in range(n):
        #    minlist[chainsize+aa] = ar[aa]
        #    maxlist[chainsize+aa] = ar[aa]

        for l in range(chainsize-1,0,-1):
            are = l << 1
            you = are + 1
            a,b = minlist[are],minlist[you]
            minlist[l] = a if a < b else b
            a,b = maxlist[are],maxlist[you]
            maxlist[l] = a if a > b else b
            
        # build complist and targets
        boundaries = [1]
        while boundaries[-1] != chainsize*2:
            boundaries.append(boundaries[-1]<<1)
        boundaries.reverse() # i+1th to ith gives the ith layer
        llb = boundaries[1:]
        rrb = boundaries[:-1]
        why = len(llb)
        for tt in range(why):
            rrb[tt] -= 1
        complist = list()
        targets = list()
        for g in range(why):
            lb,rb = llb[g],rrb[g]
            targets.append((rb-lb+1)//2)
            complist.append(sum([maxlist[j] <= minlist[j+1] for j in range(lb,rb,2)]))

        m = len(complist)
        mask = (1<<m)-1
        for u in range(m):
            if complist[u] == targets[u]: mask ^= two[u]
        #anslist.append(ansd[mask])
        endme.write(str(1<<(mask.bit_length()-1) if mask else 0))
        endme.write(" ")
        # now the hard part of doing the queries
        baseincrement = chainsize

        # redeclare these to be local (look I've been at this problem for a fucking nine or so hours and I don't understand why tf gemini keeps suggesting this but at a certain point i should be afforded the slightest bit of mercy for this utter shitshow of a problem.)
        l_min = minlist
        l_max = maxlist
        l_comp = complist
        l_targ = targets

        while q:
            q -= 1
            index,x = readints()
            index += baseincrement
            
            pa = index & ~1
            pb = pa | 1
            # actual case, first solve initial array
            if l_max[pa] <= l_min[pb]: l_comp[0] -= 1
                    
            # update values and comps
            l_min[index] = x
            l_max[index] = x
        
            if l_max[pa] <= l_min[pb]: l_comp[0] += 1

            if l_comp[0] == l_targ[0]: mask &= ~1 
            else: mask |= 1
        
            # now iterate through the remaining sublists
            for j in range(1,m):
                #lb,rb = llb[j],rrb[j] # rb is last in layer
                index >>= 1 # new updating index
                pa = index & ~1
                pb = pa | 1
                if index == 0: break
            
                if l_max[pa] <= l_min[pb]: l_comp[j] -= 1
               
                lc = index<<1
                rc = lc | 1
                a,b = l_min[lc],l_min[rc]
                c,d = l_max[lc],l_max[rc]
                l_min[index] = a if a < b else b 
                l_max[index] = c if c > d else d 

                if l_max[pa] <= l_min[pb]: l_comp[j] += 1
            
                if l_comp[j] == l_targ[j]: mask &= ~two[j]
                else: mask |= two[j]
                
            endme.write(str(1<<(mask.bit_length()-1) if mask else 0))
            endme.write(" ")
    #sys.stdout.write(" ".join(map(str,anslist)))
    sys.stdout.write(endme.getvalue())
        
main()
