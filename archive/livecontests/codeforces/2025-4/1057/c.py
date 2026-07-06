import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
track all doubles possible

there can be up to two unpaired sides if an even number of sticks is used
for odd number, only one unpaired side is allowed

"""
hv = 7487384
for _ in range(readint()):
    n = readint()
    ar = readar()
    d = {}
    for i in ar:
        if d.get(i^hv) == None: d[i^hv] = 0
        d[i^hv] += 1
    single = list()
    paircount = 0
    ans = 0
    for j in d.keys():
        if d[j] % 2 == 1: single.append(j^hv)
        paircount += d[j]//2*2
        ans += (j^hv)*(d[j]//2*2)
    if paircount == 0: print(0) # impossible
    else: # try to add 1 or 2 extra edges
        # 1 edge
        md = ans
        singlebest = 0
        for s in single:
            if s < md: singlebest = max(s,singlebest)
        # 2 edges
        single.sort()
        twobest = 0
        for k in range(len(single)-1):
            if (single[k+1]-single[k]) < md:
                twobest = max(twobest,single[k+1]+single[k])
        if singlebest == 0 and twobest == 0 and paircount == 2: print(0)
        else: print(ans+max(singlebest,twobest))
