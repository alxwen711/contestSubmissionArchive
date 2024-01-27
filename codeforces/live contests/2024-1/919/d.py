import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
offline process, then process backwards from full array
if query 2 (go to next node) mod all by the length
then check each array segment
has to be AT MOST 60 subarray passes
"""

class node:
    def __init__(self):
        self.len = 0
        self.sublen = 0
        self.vals = []

for _ in range(readint()):
    n,q = readints()
    ops = list()
    for _ in range(n):
        a,b = readints()
        ops.append((a,b))
    ar = readar()
    br = list()
    for i in range(len(ar)):
        br.append((ar[i]-1,i))
    br.sort()
    #create the array representation
    cr = list()
    cr.append(node())
    for j in ops:
        if cr[-1].len > 10000000000000000000: break #no need to go further
        v = j[1]
        if j[0] == 1:
            cr[-1].vals.append(v)
            cr[-1].sublen += 1
            cr[-1].len += 1
        elif cr[-1].sublen != 0: #create new node
            nn = node()
            nn.len = cr[-1].len*(v+1)
            cr.append(nn)
        else: #just increment last node
            cr[-1].len *= (v+1)

    #cycle nodes backwards to generate ans
    ans = [0]*q
    cr.reverse()
    #for iii in range(len(cr)):
    #    print(cr[iii].len,cr[iii].sublen,cr[iii].vals)

    for k in range(len(cr)):
        l = cr[k].len
        #print(br)
        if l <= br[-1][0]: # remap required
            dr = list()
            for a in br:
                ni = a[0] % l
                if l-ni <= cr[k].sublen: #contained in this segment
                    ans[a[1]] = cr[k].vals[ni-l]
                else:
                    dr.append((ni,a[1]))
            br = dr
            br.sort()
        else: #check for encapsulation
            while len(br) != 0:
                if l-br[-1][0] <= cr[k].sublen: #contained in this segment
                    ans[br[-1][1]] = cr[k].vals[br[-1][0]-l]
                    br.pop()
                else: break
        if len(br) == 0: break
    #any values not completed will be contained in the last array
    #for e in br:
    #    ans[e[1]] = cr[-1].vals[e[0] % cr[-1].sublen]
    print(*ans)
