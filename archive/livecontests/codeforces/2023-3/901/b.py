import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
is b brute forcable? NO
based on submission analyis, very unlikely that B is brute forcable
(still maybe useful to implement)

y is only changeable by xor setups
so given x and m, y can only be:

y
y ^ x
y ^ m
y ^ x ^ m

can only 1 cycle of y values lead to a given x value?
if x does not have bit and y does not have bit, then must do y ^ m
to get the bit (if m has it, else impossible), then x | y

what x values are even possible?
"""

def printb(ar):
    br = list()
    for i in ar:
        br.append((bin(i[0])[2:],bin(i[1])[2:]))
    print(br)
    
def solve(a,b,c,d,m):
    #for now just brute force to see what cases are even possible
    # time improvement is to swap tuples with base 10**10
    hit = {}
    hit[(a,b)] = 0
    ar = [(a,b)]
    xhit = {}
    #printb(ar)
    while True: #hit.get((c,d)) == None:
        if len(ar) == 0:
            break
            return -1 #no more continuations
        br = list()
        for i in ar:
            x,y = i[0],i[1]
            v = hit[(x,y)]
            if xhit.get(x) == None: xhit[x] = v
            if hit.get((x&y,y)) == None:
                hit[(x&y,y)] = v+1
                br.append((x&y,y))
            if hit.get((x|y,y)) == None:
                hit[(x|y,y)] = v+1
                br.append((x|y,y))
            if hit.get((x,y^x)) == None:
                hit[(x,y^x)] = v+1
                br.append((x,y^x))
            if hit.get((x,y^m)) == None:
                hit[(x,y^m)] = v+1
                br.append((x,y^m))
        #printb(br)
        ar = br
    cr = list(xhit.keys())
    cr.sort()
    dr = list()
    for snth in cr:
        dr.append((snth,xhit[snth]))
    return dr
    #return hit[(c,d)]
    


for i in range(readint()):
    a,b,c,d,m = readints()
    print(solve(a,b,c,d,m))
