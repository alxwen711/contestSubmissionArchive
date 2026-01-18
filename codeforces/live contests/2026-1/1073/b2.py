import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
using b1, the sum of every regular subsequence is computable reasonably fast

all length 2 -> base totals
length 4 -> take current totals, sum previous

dp state; either include it or don't

brute forcing is probably unreasonable

scenario where the score is not n-2?

[a,b,c,d] [e,f,g,h]
c < e
b > f

above 2 cannot hold because b < c and e < f

so all scores are either 0 or n-2
n-2 is if 2nd last ( is later than the first )

some sort of dp is then involved
last (, 2nd last (, first ), ( count - ) count, length
technically O(n**5), but no chance the full space is used (or even close)
valid if 2nd last ( > first ) AND count is 0

the score needs more info to properly be counted here??

it turns out if/else rules are hard

TLE, group counts and lengths together?

Update: There exists O(n**3)
"""

m = 998244353

#base = (-1,-1,1000000,0)

#def unhash(x):
#    return x//8000000 % 200,x//40000 % 200,x//200 % 200,x % 200

#def rehash(a,b,c,d):
#    return a*8000000+b*40000+c*200+d


base = 1599999800

bbb = [40000*ii for ii in range(101)]
ccc = [200*ii for ii in range(101)]

for _ in range(readint()):
    n = readint()
    s = readin()
    ans = 0
    count = {}
    count[base] = 1
    length = {}
    length[base] = 0
    mv = s.count(")") # upper limit
    for i in range(n):
        ncount = {}
        nlength = {}
        for d in count.keys():
            # v = number of lists, w = length of lists combined
            v,w = count[d],length[d]
            a,b,c,t = d//8000000 % 200,d//40000 % 200,d//200 % 200,d % 200
            # try as is
            if t <= mv:
                if ncount.get(d) == None:
                    ncount[d] = v
                    nlength[d] = w
                else:
                    ncount[d] = (ncount[d]+v) % m
                    nlength[d] = (nlength[d]+w) % m
            # try adding the character
            if s[i] == "(" and t < mv:
                if b > c and b != 199: # if already "solved", don't bother
                    nv = bbb[b]+ccc[c]+t+1
                    if ncount.get(nv) == None:
                        ncount[nv] = v
                        nlength[nv] = v + w
                    else:
                        ncount[nv] = (ncount[nv]+v) % m
                        nlength[nv] = (nlength[nv]+w+v) % m
                else:
                    nv = i*8000000+bbb[a]+ccc[c]+t+1
                    if ncount.get(nv) == None:
                        ncount[nv] = v
                        nlength[nv] = v+w
                    else:
                        ncount[nv] = (ncount[nv]+v) % m
                        nlength[nv] = (nlength[nv]+w+v) % m
            elif s[i] == ")" and t != 0:
                nv = d-1
                if c == 199:
                    if b > i and b != 199: nv = b*40000+i*200+t-1
                    else: nv = a*8000000+bbb[b]+ccc[]+t-1
                if ncount.get(nv) == None:
                    ncount[nv] = v
                    nlength[nv] = v+w
                else:
                    ncount[nv] = (ncount[nv]+v) % m
                    nlength[nv] = (nlength[nv]+w+v) % m
        count = ncount
        length = nlength
        if s[i] == ")": mv -= 1 # upper limit
    for d in count.keys():
        b,c,t = d//40000 % 200,d//200 % 200,d % 200
        if b != 199 and b > c and t == 0:
            ans += length[d]-(count[d]*2)
    print(ans % m)
