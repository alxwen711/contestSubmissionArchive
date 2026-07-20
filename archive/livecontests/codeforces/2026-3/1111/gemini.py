import sys
from io import StringIO
from array import array

def main():
    two = [1]
    for _ in range(24):
        two.append(two[-1] << 1)
    endme = StringIO()
    
    readin = sys.stdin.buffer.readline
    try:
        t_cases = int(readin())
    except (IOError, ValueError):
        return

    for _ in range(t_cases):
        n, q = map(int, readin().split())
        ar = list(map(int, readin().split()))
        while len(ar) < n:
            ar.extend(map(int, readin().split()))

        if n == 1:
            endme.write("0 ")
            for _ in range(q):
                readin()
                endme.write("0 ")
            continue

        chainsize = 1
        while chainsize < n:
            chainsize <<= 1

        intscore = 2**30
        
        # Using fast, contiguous C-arrays instead of standard Python lists
        minlist = array('i', [intscore]) * (chainsize * 2)
        maxlist = array('i', [0]) * (chainsize * 2)

        for aa in range(n):
            minlist[chainsize + aa] = ar[aa]
            maxlist[chainsize + aa] = ar[aa]
        for aa in range(n, chainsize):
            minlist[chainsize + aa] = intscore
            maxlist[chainsize + aa] = intscore

        for l in range(chainsize - 1, 0, -1):
            are = l << 1
            you = are + 1
            a, b = minlist[are], minlist[you]
            minlist[l] = a if a < b else b
            a, b = maxlist[are], maxlist[you]
            maxlist[l] = a if a > b else b
            
        boundaries = [1]
        while boundaries[-1] != chainsize * 2:
            boundaries.append(boundaries[-1] << 1)
        boundaries.reverse()
        
        llb = boundaries[1:]
        rrb = boundaries[:-1]
        why = len(llb)
        rrb_fixed = [r - 1 for r in rrb]
        
        complist = []
        targets = []
        for g in range(why):
            lb, rb = llb[g], rrb_fixed[g]
            targets.append((rb - lb + 1) // 2)
            
            # Initial count of sorted sibling pairs
            c = 0
            for j in range(lb, rb, 2):
                if maxlist[j] <= minlist[j + 1]:
                    c += 1
            complist.append(c)

        m = len(complist)
        mask = (1 << m) - 1
        for u in range(m):
            if complist[u] == targets[u]: 
                mask ^= two[u]
                
        endme.write(str(1 << (mask.bit_length() - 1) if mask else 0) + " ")
        baseincrement = chainsize

        l_min = minlist
        l_max = maxlist
        l_comp = complist
        l_targ = targets

        for _ in range(q):
            index, x = map(int, readin().split())
            index += baseincrement
            
            # --- LAYER 0 ---
            pa = index & ~1
            pb = pa | 1
            if l_max[pa] <= l_min[pb]: 
                l_comp[0] -= 1
                    
            l_min[index] = x
            l_max[index] = x
        
            if l_max[pa] <= l_min[pb]: 
                l_comp[0] += 1

            if l_comp[0] == l_targ[0]: 
                mask &= ~1 
            else: 
                mask |= 1
        
            # --- SUBTREE CLIMBING LAYERS ---
            for j in range(1, m):
                index >>= 1  # Move up to parent
                
                # 1. Identify the parent's sibling layout position on layer j BEFORE changing anything
                pa = index & ~1
                pb = pa | 1
                
                # 2. Subtract based on the OLD parent value state
                if l_max[pa] <= l_min[pb]: 
                    l_comp[j] -= 1
               
                # 3. NOW update the parent's actual minimum and maximum from its children
                lc = index << 1
                rc = lc | 1
                a, b = l_min[lc], l_min[rc]
                c, d = l_max[lc], l_max[rc]
                l_min[index] = a if a < b else b 
                l_max[index] = c if c > d else d 

                # 4. Add back to the counter based on the NEW parent value state
                if l_max[pa] <= l_min[pb]: 
                    l_comp[j] += 1
            
                if l_comp[j] == l_targ[j]: 
                    mask &= ~two[j]
                else: 
                    mask |= two[j]
                
            endme.write(str(1 << (mask.bit_length() - 1) if mask else 0) + " ")
        endme.write("\n")
        
    sys.stdout.write(endme.getvalue())
        
if __name__ == '__main__':
    main()