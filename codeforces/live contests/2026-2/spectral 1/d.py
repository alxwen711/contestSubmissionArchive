import sys
from random import shuffle,randint

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
possibly some sort of dp?

inversion score is start point to just before end point,
take sum of values in a given array

generally ANY positive value in the array indicates an inversion
there are cases where negatives are allowed (total sum would still
be a net positive)

any subarray that is positive should be an inversion

ranking system can be created in O(n^2), unsure if every edge is needed

the first passthrough can tell a valid number the first value could be

feels somewhat like quicksort, possible for bad roll to occur
"""

anslist = list()

for _ in range(readint()):
    n = readint()
    br = readar()
    prefix = [0]
    for i in br:
        prefix.append(prefix[-1]+i)
    ans = [0]*n
    v = [i for i in range(n)]
    shuffle(v)
    base = set()
    for snth in v:
        base.add(snth)
    q = [base]
    qq = [1]
    while len(q) != 0:
        ar = q.pop()
        l = qq.pop()
        h = len(ar)+l-1
        if l == h:
            ans[ar.pop()] = l
            continue
        elif l+1 == h: # two value case
            a = ar.pop()
            b = ar.pop()
            if a > b: a,b = b,a
            t = prefix[b]-prefix[a]
            if t > 0 or (t == 0 and randint(1,2) == 1):
                ans[a] = h
                ans[b] = l
            else:
                ans[a] = l
                ans[b] = h
            continue
        pivot = ar.pop()
        lower = set()
        higher = set()
        for i in ar:
            if i < pivot:
                t = prefix[pivot]-prefix[i]
                if t > 0 or (t == 0 and randint(1,2) == 1): # we want an inversion, i > pivot
                    higher.add(i)
                else:
                    lower.add(i)
            else:
                t = prefix[i]-prefix[pivot]
                if t > 0 or (t == 0 and randint(1,2) == 1):
                    lower.add(i)
                else:
                    higher.add(i)
        val = l + len(lower)
        ans[pivot] = val
        if len(lower) != 0:
            q.append(lower)
            qq.append(l)
        if len(higher) != 0:
            q.append(higher)
            qq.append(val+1)
    
    #solve(ans,base,1,n,prefix)
    anslist.append(" ".join(list(map(str,ans))))

sys.stdout.write("\n".join(anslist))
