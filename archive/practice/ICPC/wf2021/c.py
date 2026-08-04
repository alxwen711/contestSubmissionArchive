import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,m = readints()
if n > 100: print("impossible")
else:
    # try ALL numerator denomiator combinations reasonable
    flag = False
    ar = [0]
    for ii in range(1,1000000):
        ar.append(ii**n)
        if ar[-1]//ii > m: break
    for d in range(2,len(ar)):
        multd = ar[d]
        for num in range(1,d):
            if gcd(num,d) != 1: continue
            # try num/d
            multn = ar[d-num]
            # multd/(multd-multn) * num/d is the starting value
            v = m*num
            if v % (multd-multn) == 0:
                flag = True
                print(num,d)
                break
        if flag: break
        d += 1
        multd = d**n
    if not flag: print("impossible")
