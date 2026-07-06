import sys
n,q = map(int, sys.stdin.readline().split())
#0-> clean, 1-> sick, 2-> unsure
h = [2]*n
ranges = list()


def check(h,a,b):
    sol = list()
    chain = 0
    st = 0
    for y in range(b-a+1):
        if h[a+y-1] == 1:
            sol.clear()
            return []
        if chain == 0:
            if h[a+y-1] == 2:
                chain += 1
                st = a+y
        else:
            if h[a+y-1] == 2:
                chain += 1
            else:
                t = list()
                t.append(st)
                t.append(st+chain-1)
                sol.append(t)
                chain = 0
    if chain != 0:
            t = list()
            t.append(st)
            t.append(st+chain-1)
            sol.append(t)
    #print(sol)
    if len(sol) == 1:
        if sol[0][0] == sol[0][1]:
            h[sol[0][0]-1] = 1
            sol.clear()
            return []
    return sol

scans = list()
for i in range(q):
    """
    keep track of ranges where there is a sick person?
    """
    ar = list(map(int, sys.stdin.readline().split()))
    if len(ar) == 4: scans.append(ar)
    else: #clear scans first
        #print(scans)
        dd = len(scans)
        for j in range(dd):
            if scans[j][3] == 0:
                for l in range(scans[j][2] - scans[j][1]+1):
                    h[scans[j][1]+l-1] = 0
        #update ranges
        cc = len(ranges)
        for m in range(cc):
            tmp = check(h,ranges[0][0],ranges[0][1])
            if tmp: ranges.append(tmp)
            ranges.pop(0)
            
        for k in range(dd):
            if scans[k][3] == 1:
                tmp = check(h,scans[k][1],scans[k][2])
                if tmp: ranges.append(tmp)
        scans.clear()
        #now check
        if h[ar[1]-1] == 0: print ("NO")
        elif h[ar[1]-1] == 1: print ("YES")
        else: print ("N/A")
#print(h)
        
