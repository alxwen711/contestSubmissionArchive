import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
each testcase is a single 100 bit string
runtime is not really a problem here
maybe make biggest swap possible and see if it's
enough to change difference each time?
1/0 count may not be close to equal, 0001000 is possible
there MUST be an even number of 0's or 1's (could be both)
if there is a large enough move, check if an exact move is actually possible
else +1


hack case: 0011110101001010000000000111100101011110100111001011000101111111010011001000110
expected output is not 2
"""

def compute(n,ar):
    z,o = 0,0 #01,10
    zp,op = 0,0
    for i in range(n):
        if ar[-i-1] == 1:
            o += zp
            op += 1
        else:
            z += op
            zp += 1
    return z-o

s = input()
n = len(s)
ar = list()
for i in range(n):
    ar.append(int(s[i]))
#zc = ar.count(0)
#oc = n-zc
sv = compute(n,ar)
#print(sv)
if sv > 0: #more 01 than 10
    ans = 0
    #leftest 0 and rightest 1 swap
    while sv > 0:
        ans += 1
        a = ar.index(0)
        b = n-1
        while ar[b] == 0:
            b -= 1
        ar[a] = 1
        ar[b] = 0
        sv = compute(n,ar)
        if sv < 0: #revert change
            ar[a] = 0
            ar[b] = 1
            break
    if sv != 0:
        flag = False
        for j in range(n-1):
            for k in range(j+1,n):
                ar[j],ar[k] = ar[k],ar[j]
                if compute(n,ar) == 0:
                    flag = True
                    break
                ar[j],ar[k] = ar[k],ar[j]
        if not flag: ans += 1
    print(ans)
elif sv < 0: #more 10 than 01
    ans = 0
    #leftest 1 and rightest 0 swap
    while sv < 0:
        ans += 1
        a = ar.index(1)
        b = n-1
        while ar[b] == 1:
            b -= 1
        ar[a] = 0
        ar[b] = 1
        sv = compute(n,ar)
        if sv > 0: #revert change
            ar[a] = 1
            ar[b] = 0
            break
    if sv != 0:
        flag = False
        for j in range(n-1):
            for k in range(j+1,n):
                ar[j],ar[k] = ar[k],ar[j]
                if compute(n,ar) == 0:
                    flag = True
                    break
                ar[j],ar[k] = ar[k],ar[j]
        if not flag: ans += 1
    print(ans)
else: #equal
    print(0)
    
