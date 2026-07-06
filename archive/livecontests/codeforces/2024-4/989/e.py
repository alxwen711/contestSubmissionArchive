import sys
from itertools import permutations
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
pairups exist
most values likely work
note cases where k is too large?
"""

def factorial(n):
    if n > 15: return 54387934785348975634789
    a = 1
    for i in range(1,n+1):
        a *= i
    return a

def solve(n,k):
    if n < 10: # not enough permutations
        a = 1
        for snth in range(1,n+1):
            a *= snth
        if a < k:
            print("NO")
            return
    if n == 1 and k == 1: # singular value, k = 1
        print("YES")
        print(1)
        return
    if k == 1: # k = 1, impossible
        print("NO")
        return
    if k == 2: # basic flip
        print("YES")
        ar = list()
        for snth in range(1,n+1):
            ar.append(snth)
        print(*ar)
        ar.reverse()
        print(*ar)
        return
    elif k == n: # cyclic shift
        print("YES")
        ar = list()
        for snth in range(n):
            tmp = list()
            for i in range(n):
                tmp.append((snth+i) % n + 1)
            ar.append(tmp)
        for a in ar:
            print(*a)
        return
    # any even will work
    # if n is odd then any even+n also works
    # at a large enough point, you can probably just choose randomly?
    # if n is even, any odd value is impossible
    # 5 3 case is impossible, unsure if n odd makes odd impossible
    # for now, assume it is? (9 3 looks like it fails as well)
    elif k % 2 == 0: # even pairing method
        print("YES")
        fv = 1
        c = 1
        while c < k:
            fv += 1
            c *= fv
        if fv == n and k != 0: # brute force ALL cases
            d = {}
            ar = list()
            for snth in range(1,fv+1):
                ar.append(snth)
            br = list(permutations(ar))
            rr = k//2
            for b in br:
                cr = list(b)
                dr = list()
                for snth in cr:
                    dr.append(n-snth+1)
                er = tuple(dr)
                if d.get(hash(b)) == None and d.get(hash(er)) == None:
                    d[hash(b)] = 1
                    d[hash(er)] = 1
                    print(*cr)
                    print(*dr)
                    rr -= 1
                    if rr == 0: break
        elif k != 0: #permutate only up to necessary
            ar = list()
            for snth in range(1,fv+1):
                ar.append(snth)
            br = list(permutations(ar))
            for i in range(k//2):
                cr = list()
                dr = list()
                for ii in br[i]:
                    cr.append(ii)
                    dr.append(n-ii+1)
                for j in range(fv+1,n+1):
                    cr.append(j)
                    dr.append(n-j+1)
                print(*cr)
                print(*dr)
        return
    elif n % 2 == 0: # odd k + even n is an auto fail
        print("NO")
        return
    elif k+1 == factorial(n): # this is apparently impossible
        print("NO")
        return
    else: # 3 + something
        print("YES")
        d = {}
        a,b,c = 1,n//2+1,n
        aa = list()
        bb = list()
        cc = list()
        for _ in range(n):
            aa.append(a)
            bb.append(b)
            cc.append(c)
            a += 1
            b += 1
            if b == n+1:
                b = 1
            c -= 2
            if c < 1: c += n
        d[hash(tuple(aa))] = 1
        d[hash(tuple(bb))] = 1
        d[hash(tuple(cc))] = 1
        print(*aa)
        print(*bb)
        print(*cc)
        fv = 1
        c = 1
        while c < k:
            fv += 1
            c *= fv
        k = k-3
        if fv == n and k != 0: # brute force ALL cases
            ar = list()
            for snth in range(1,fv+1):
                ar.append(snth)
            br = list(permutations(ar))
            rr = k//2
            for b in br:
                cr = list(b)
                dr = list()
                for snth in cr:
                    dr.append(n-snth+1)
                er = tuple(dr)
                if d.get(hash(b)) == None and d.get(hash(er)) == None:
                    d[hash(b)] = 1
                    d[hash(er)] = 1
                    print(*cr)
                    print(*dr)
                    rr -= 1
                    if rr == 0: break
        elif k != 0: #permutate only up to necessary
            ar = list()
            for snth in range(1,fv+1):
                ar.append(snth)
            br = list(permutations(ar))
            rr = k//2
            for i in range(len(br)):
                cr = list()
                dr = list()
                for ii in br[i]:
                    cr.append(ii)
                    dr.append(n-ii+1)
                for j in range(fv+1,n+1):
                    cr.append(j)
                    dr.append(n-j+1)
                if d.get(hash(tuple(cr))) == None and d.get(hash(tuple(dr))) == None:
                    print(*cr)
                    print(*dr)
                    d[hash(tuple(cr))] = 1
                    d[hash(tuple(dr))] = 1
                    rr -= 1
                    if rr == 0: break
        return

for _ in range(readint()):
    n,k = readints()
    solve(n,k)
