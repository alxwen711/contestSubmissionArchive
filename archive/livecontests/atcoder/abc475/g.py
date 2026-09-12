import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the highest value normally used is 37
realistically nothing above 100 in prime factors is necessary
recursive search may be possible, keep some sort of conditional

E? F? LMAO

D doesn't need full prime factorization, only needs to check primes
up to about 100

search area is not as large as it seems?

current value used
maximum value allowed
what the next prime to try is (index, stop at 25)
restriction value (-1 means none, otherwise positive value indicates how many left)
restrictions
score (number of factors currently)

alternate idea is to find the maximum exponent allowed and only try within 4/5
this is with an added condition of the following:

2 exponent maximum is 10
3 exponent maximum is 6
everything else caps out at 5

there is some weird case where the 2 can be a very low exponent in last example
"""
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def search(val,n,index,r,restrictions,s):
    pval = primes[index]
    ans = s
    bv = val

    # determine the maximum usable exponent
    tmp = val*pval
    maxep = 0
    while tmp <= n:
        maxep += 1
        tmp *= pval
    if pval == 2: maxep = min(maxep,10)
    elif pval == 3: maxep = min(maxep,7)
    elif pval == 5: maxep = min(maxep,5)
    elif pval == 7: maxep = min(maxep,3)
    elif pval < 15: maxep = min(maxep,2)
    else: maxep = min(maxep,1)
    if r == 1 and restrictions.get(pval) != None: # prevent violation of div
        maxep = min(maxep,restrictions[pval]-1)
    
    if restrictions.get(pval) == None or r == -1: # freely run as many as possible
        for ex in range(maxep,-1,-1):
            nval = val*(pval**ex) 
            ns = s*(ex+1)
            if index == 24:
                if ns > ans:
                    ans = ns
                    bv = nval
            else:
                nv,x = search(nval,n,index+1,r,restrictions,ns)
                if nv > ans:
                    ans = nv
                    bv = x
            
    else: # check the restriction
        over = restrictions[pval]
        flag = False
        for ex in range(maxep,-1,-1):
            nval = val*(pval**ex) 
            #if pval == 2: print(ex,"exp of 2 being run here")
            ns = s*(ex+1)
            if index == 24:
                if ns > ans:
                    ans = ns
                    bv = nval
            else:
                if ex < over:
                    nv,x = search(nval,n,index+1,-1,restrictions,ns)
                    if nv > ans:
                        ans = nv
                        bv = x
                else:
                    nv,x = search(nval,n,index+1,r-1,restrictions,ns)
                    if nv > ans:
                        ans = nv
                        bv = x
    return ans,bv
    
for _ in range(readint()):
    n,d = readints()
    rc = 0
    restrictions = {}
    for p in primes:
        if d % p == 0:
            rc += 1
            cc = 0
            while d % p == 0:
                cc += 1
                d //= p
            restrictions[p] = cc
    print(search(1,n,0,rc,restrictions,1)[1])
