import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
even -> /2
odd -> +1

some sort of bit set logic
only a certain set of values is actually possible

brute force down each value, store into a dict setup

no hacks, might not need antihashing?

everything needs to be hit, definitely do not need to track all
"""


anslist = list()
for _ in range(readint()):
    n = readint()
    ar = readar()
    d = {} # move dict
    cc = {} # count dict
    flag = True
    for i in ar:
        v = i
        c = 0
        if v == 1:
            if d.get(1) == None:
                d[1] = 0
                cc[1] = 0
            if d.get(2) == None:
                d[2] = 0
                cc[2] = 0
            d[2] += 1
            cc[1] += 1
            cc[2] += 1
            
        else:
            if flag:
                if d.get(v) == None:
                    d[v] = 0
                    cc[v] = 0
                cc[v] += 1
            elif d.get(v) != None:
                cc[v] += 1
            while v != 1:
                c += 1
                if v % 2 == 0: v //= 2
                else: v += 1
                if flag:
                    if d.get(v) == None:
                        d[v] = 0
                        cc[v] = 0
                    d[v] += c
                    cc[v] += 1
                elif d.get(v) != None:
                    d[v] += c
                    cc[v] += 1
        flag = False
    ans = 999999999999999999999999999
    for u in d.keys():
        if cc[u] == n: ans = min(ans,d[u])
    anslist.append(str(ans))
            
sys.stdout.write("\n".join(anslist))
            
        
