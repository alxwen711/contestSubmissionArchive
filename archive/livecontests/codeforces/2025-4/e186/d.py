import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
possible optimal is to greed
remove from box p_i if possible, else remove from box 0
max value from box 1 to n -> number of rounds

12 cases in example 4:
2xxx (6 options)
3xxx (6 options)


12345
optimal: 54321 (6 needed)
51234 (6 needed)
45321 (7 needed)
43215 (10 needed)
15432 (7 needed)

only positioning of the highest values matter
"""

m = 998244353

facts = [1]
invs = [1]

from copy import deepcopy

for i in range(1,100):
    facts.append((facts[-1]*i) % m)
    invs.append(pow(facts[-1],m-2,m))

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = deepcopy(ar[1:])
    br.sort()
    mv = 0
    for i in range(n):
        mv += max(br[-1]-br[i]-1,0)
    #print(mv)
    if mv > ar[0]: print(0)
    else:
        padding = ar[0]-mv
        d = {}
        for j in br:
            if d.get(j) == None: d[j] = 0
            d[j] += 1
        mm = max(br)
        maxcount = d[mm]
        
        # count ways to arrange everything else
        base = facts[n-maxcount]

        # figure out the rest of this
        area = min(n,maxcount+padding)
        print((base*facts[area]*invs[area-maxcount]) % m)



        
