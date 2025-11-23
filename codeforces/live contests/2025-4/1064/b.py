import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
O(n^2) will work
any mode can be selected
only frequency of the values actually matters
1 -> 1
11 -> 2
12 -> 3
111 -> 3
122 -> 4
1222 -> 6 (2,12,22,122,222,1222)
1122 -> 8 (1,2,11,12,22,112,122,1122)
123 -> 7
1233 -> 8 (3,13,23,12,123,133,233,1233)
12333 -> 12 (3,13,23,33,123,133,233,333,1233,1333,2333,12333)

1 = 1
2 = 2
11 = 3
3 = 3
21 = 4
31 = 6
22 = 8
111 = 7
211 = 8
311 = 12
4321 = 111
3331 = 126
"""

m = 998244353

for _ in range(readint()):
    n = readint()
    ar = readar()
    d = {}
    for i in ar:
        if d.get(i) == None: d[i] = 0
        d[i] += 1
    br = list() # list of frequencies
    for u in d.keys():
        br.append(d[u])
    cr = list() # highest to lowest frequency values and their frequencies
    d = {}
    for i in br:
        if d.get(i) == None: d[i] = 0
        d[i] += 1
    for u in d.keys():
        cr.append((u,d[u]))
    cr.sort()
    cr.reverse()
    dp = {}
    dp[999999] = 1
    print(cr)
    for c in cr:
        ndp = {}
        for d in dp.keys():
            maxv,exp,cc = min(d,c[0]),c[1],dp[d]
            #maxv,exp,cc = c[0],c[1],dp[d]
            #for a in range(maxv+1):
            for a in range(maxv,-1,-1):
                # assume the next maxv dp value is a
                # count = (pow(maxv+1-a,exp,m)-pow(maxv-a,exp,m)) % m
                count = (pow(a+1,exp,m)-pow(a,exp,m)) % m
                target = a
                #if d != 999999: target = max(a,d)
                if ndp.get(target) == None: ndp[target] = 0
                ndp[target] = (ndp[target]+count*cc) % m
        dp = ndp
        print(dp)
    ans = -1
    for ii in dp.keys():
        ans = (ans+dp[ii]) % m
    print(ans)

    
