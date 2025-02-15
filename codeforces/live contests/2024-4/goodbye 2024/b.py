import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n = readint()
    d = {}
    ar = list()
    for _ in range(n):
        l,r = readints()
        if l == r:
            if d.get(l) == None: d[l] = 1
            else: d[l] += 1
        ar.append((l,r))
    ans = list()
    no = list(d.keys())
    no.sort()
    nod = {}
    #print(no)
    #print(d)
    for ii in range(len(no)):
        nod[no[ii]] = ii
    for r in ar:
        lp = r[0]
        rp = r[1]
        ansl = nod.get(lp,9999999999999999999999999999999999999999999)
        ansr = nod.get(rp,-9999999999999999999999999999999999999999999)
        """
        ansl = -1
        ansr = -1
        # lp
        low = 0
        high = len(no)-1
        while high-low > 1:
            mid = (low+high)//2
            if no[mid] >= lp: high = mid
            else: low = mid
        if no[low] >= lp: ansl = low
        elif no[high] >= lp: ansl = high
        else: ansl = high+1

        # rp
        low = 0
        high = len(no)-1
        while high-low > 1:
            mid = (low+high)//2
            if no[mid] <= rp: low = mid
            else: high = mid
        if no[high] <= rp: ansr = high
        elif no[low] <= rp: ansr = low
        else: ansr = low-1
        """
        if ansr-ansl+1 == rp-lp+1:
            if lp == rp and d.get(lp) == 1: ans.append(1)
            else: ans.append(0)
        else: ans.append(1)
    print(*ans,sep="")



        
