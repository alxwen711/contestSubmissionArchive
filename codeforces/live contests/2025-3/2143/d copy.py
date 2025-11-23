import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of sequences that have at most one decrement?

1 2 3 4 5 3 2 is impossible
1 3 1 3 1 3 is possible (RBRBRB)
track the highest value that is R (colour as many as possible R)
1 3 1 5 1 7 1 6 1
on first decrease, track the maximum recorded from 0 case and cur val as min
then all other values need to diverge out from this

4 2 1 is impossible
4 2 5

track highest that was coloured R/B
this is now counting number of possible sequences
"""

m = 1000000007
for _ in range(readint()):
    n = readint()
    ar = readar()

    d = {}
    d[(-1,-1)] = 1

    for a in ar:
        nd = {}
        for i in d.keys():
            v = d[i]
            if nd.get(i) == None: nd[i] = 0
            nd[i] = (nd[i] + v) % m
            # red
            if a >= i[0]:
                if nd.get((max(i[0],a),i[1])) == None: nd[(max(i[0],a),i[1])] = 0
                nd[(max(i[0],a),i[1])] = (nd[(max(i[0],a),i[1])]+v) % m
            # blue
            if a >= i[1]:
                if nd.get((i[0],max(i[1],a))) == None: nd[(i[0],max(i[1],a))] = 0
                nd[(i[0],max(i[1],a))] = (nd[(i[0],max(i[1],a))]+v) % m
        d = nd
    ans = 0
    for snth in d.keys():
        ans = (ans+d[snth]) % m
    print(ans)






                
