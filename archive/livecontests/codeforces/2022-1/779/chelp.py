from itertools import permutations

def m(p,k):
    ans = 0
    ma = 0
    x = len(p)
    for f in range(x):
        if p[(f-k)%x] > ma:
            ma = p[(f-k)%x]
            ans += 1
    return ans


l = 7
ar = list()
for i in range(l):
    ar.append(i+1)
p = list(permutations(ar))
for j in range(720): #4 factorial
    tmp = list()
    for k in range(l):
        tmp.append(m(p[j],k))
    if tmp.count(4) > 1 and max(tmp) == 4: print(tmp)
