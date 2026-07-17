import sys
from copy import deepcopy
from itertools import permutations

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
valid length 3 sequences (24 total)
000
001
002
003
010
011
012
013
020
021
022
023
...

basically any sequence where a_i <= i can be valid

{1: 2}
{1: 5, 2: 1}
{1: 15, 2: 6, 3: 2, 4: 1}

6 -> 33405
7 -> 517857
2
5,1
15,6,2,1
54,28,15,12,3,4,2,1,1
235,126,82,86,31,46,26,25,15,10,5,11,3,5,4,3,1,2,1,0,1
"""

# create all possible sequences
n = 4
ar = [[]]
for i in range(n):
    br = list()
    for j in ar:
        for k in range(i+2):
            cr = deepcopy(j)
            cr.append(k)
            br.append(cr)
    ar = br

# create all removal possibilities
er = list()
for e in range(1,n+1):
    er.append(e)

pr = [[()]]
for k in range(1,n+1):
    pr.append(list(permutations(er,k)))
dd = {}
ans = 0
for a in ar:
    tmp = 0
    for p in pr[n-a.count(0)]:
        index = 0
        flag = True
        for u in range(n):
            if a[u] != 0:
                if p[index] > (u+1) or p[index] < a[u]:
                    flag = False
                    break
                index += 1
        if flag: tmp += 1
    print(a,tmp)
    ans += tmp
    if dd.get(tmp) == None: dd[tmp] = 0
    dd[tmp] += 1
print(ans) 
print(dd)


#for _ in range(readint()):
#    n,m = readints()
