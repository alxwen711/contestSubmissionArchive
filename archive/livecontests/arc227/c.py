import sys
from random import randint

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if all same character (aaaa) then k = n, no improvement possible

some sort of cyclic nature defines optimal k
abcabc (2)
bcabbcab (2)
aabb (1)
bcbacbca (1?, needs 3+ moves)
___a___a
_c__c___
____c_ca
_______a
there are only 26 lowercase letters, is it possible to run efficient bfs?

n <= 1000

do we assume that each letter should only be used once?
after second step, there are probably some sort of subset removals possible
you do NOT have to find the optimal sequence

(might be best to try choosing the minimal count first, then
could we just randomize this until we hit the answer?

knowing the problem there's probably a testcase where
using 'b' operation 100 times in a row is required

at this point I'm unsure if the cycle assumption is even correct
"""

def cyclic(n,s,x):
    # x is the number of cycles
    cl = n//x
    for a in range(cl):
        for b in range(x-1):
            if s[b*cl+a] != s[b*cl+a+cl]: return False
    return True
        
def compute(ar,br):
    n,m = len(ar),len(br)
    hit = 0
    ans = list()
    if ar[-1] >= br[-1]:
        ans.append(br[0])
    for ii in range(m):
        flag = False
        while hit != n:
            if br[ii] > ar[hit]:
                flag = True
                hit += 1
            else: break
        if flag:
            if ii == 0:
                if ans == []: ans.append(br[ii])
            else: ans.append(br[ii])
    return ans
    


n = readint()
s = readin()
ans = 1
for i in range(2,n+1):
    if n % i == 0:
        if cyclic(n,s,i): ans = i
print(ans)
if ans != n:
    # convert to a 1 problem
    s = s[:n//ans]
    n //= ans
    options = list()
    d = {}
    for i in range(n):
        if d.get(s[i]) == None:
            options.append(s[i])
            d[s[i]] = list()
        d[s[i]].append(i)
    nn = len(options)
    ans = list()
    indexlist = [i for i in range(n)]
    for _ in range(1000000):
        nv = randint(0,nn-1)
        indexlist = compute(indexlist,d[options[nv]])
        ans.append(options[nv])
        if len(indexlist) == 1: break        
    print(len(ans))
    print(*ans,sep="")
else:
    print(0)
    print()

