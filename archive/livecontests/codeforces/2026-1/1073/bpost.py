import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Post contest implementation; O(n**3) sol

All of the previous observations are simplifiable to
if the RBS has subseq ")((" in it

state, ( count - ) count

state can be 0,1,2,3
0 -> 1 if )
1 -> 2 if (
2 -> 3 if ( (done)
1,2 -> 1 if )

update: this is actually O(n**2), n <= 100 constraint very much
mental blocked me here assuming constraint meant O(n**4) ideas were a thing,
not even considering O(n**2)

This can technically go even faster with using array + hashing setups
"""

m = 998244353

base = (0,0)
for _ in range(readint()):
    n = readint()
    s = readin()
    count = {}
    count[base] = 1
    length = {}
    length[base] = 0
    ans = 0
    for i in range(n):
        ncount = {}
        nlength = {}
        for d in count.keys():
            a,b,v,w = d[0],d[1],count[d],length[d]
            # no add case
            if ncount.get(d) == None:
                ncount[d] = 0
                nlength[d] = 0
            ncount[d] = (ncount[d]+v) % m
            nlength[d] = (nlength[d]+w) % m
            # add case
            if s[i] == "(":
                nv = (a,b+1)
                if a == 1 or a == 2: nv = (a+1,b+1)
                if ncount.get(nv) == None:
                    ncount[nv] = 0
                    nlength[nv] = 0
                ncount[nv] = (ncount[nv]+v) % m
                nlength[nv] = (nlength[nv]+w+v) % m
            elif b > 0:
                nv = (a,b-1)
                if a == 0: nv = (1,b-1)
                if ncount.get(nv) == None:
                    ncount[nv] = 0
                    nlength[nv] = 0
                ncount[nv] = (ncount[nv]+v) % m
                nlength[nv] = (nlength[nv]+w+v) % m
        count = ncount
        length = nlength
    if count.get((3,0)) != None:
        print((length[(3,0)]-(count[(3,0)]*2)) % m)
    else: print(0)
