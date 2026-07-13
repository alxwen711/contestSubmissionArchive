import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
1100 is infeasible
111000 is infeasible
11110000 fails
1111100000 fails
"""

twoval = 64
setval = 56

pv = list()
for i in range(twoval):
    if i | setval == setval or i & setval == setval: pv.append(i)

#pv = [0,4,8,12,13,14,15]
print(pv)

sets = list()

for i in range(twoval):
    ar = set()
    for p in pv:
        ar.add(p^i)
    sets.append(ar)


minflag = 9999999
ansa,ansb = -1,-1
for a in range(twoval-1):
    for b in range(a+1,twoval):
        flag = 0
        for c in sets[a]:
            if c in sets[b]:
                flag += 1
        if flag <= minflag:
            print(a,b)
            ansa,ansb = a,b
            minflag = flag

print(ansa,ansb)
