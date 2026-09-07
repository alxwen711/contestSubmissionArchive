import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
try to match odd with even
place largest values at the ends
just try forcing largest odds, largest evens, largest one of each
"""

def f(n,ar):
    v = 0
    for i in range(n-1):
        v += (ar[i]+ar[i+1])//2
    return v

for _ in range(readint()):
    n = readint()
    ar = readar()
    even = list()
    odd = list()
    for i in ar:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    even.sort()
    odd.sort()
    ans = 8745286582652658265825
    if len(even) != 0 and len(odd) != 0:
        ar = deepcopy(even)
        br = deepcopy(odd)
        ending = br.pop()
        ansl = list()
        for ii in range(n-1):
            if ii % 2 == 0:
                if len(ar) != 0: ansl.append(ar.pop())
                else: ansl.append(br.pop())
            else:
                if len(br) != 0: ansl.append(br.pop())
                else: ansl.append(ar.pop())
        ansl.append(ending)
        ans = min(ans,f(n,ansl))
        ar = deepcopy(odd)
        br = deepcopy(even)
        ending = br.pop()
        ansl = list()
        for ii in range(n-1):
            if ii % 2 == 0:
                if len(ar) != 0: ansl.append(ar.pop())
                else: ansl.append(br.pop())
            else:
                if len(br) != 0: ansl.append(br.pop())
                else: ansl.append(ar.pop())
        ansl.append(ending)
        ans = min(ans,f(n,ansl))
    if len(even) > 1:
        ar = deepcopy(even)
        br = deepcopy(odd)
        ending = ar.pop()
        ansl = list()
        for ii in range(n-1):
            if ii % 2 == 0:
                if len(ar) != 0: ansl.append(ar.pop())
                else: ansl.append(br.pop())
            else:
                if len(br) != 0: ansl.append(br.pop())
                else: ansl.append(ar.pop())
        ansl.append(ending)
        ans = min(ans,f(n,ansl))
    if len(odd) > 1:
        ar = deepcopy(odd)
        br = deepcopy(even)
        ending = ar.pop()
        ansl = list()
        for ii in range(n-1):
            if ii % 2 == 0:
                if len(ar) != 0: ansl.append(ar.pop())
                else: ansl.append(br.pop())
            else:
                if len(br) != 0: ansl.append(br.pop())
                else: ansl.append(ar.pop())
        ansl.append(ending)
        ans = min(ans,f(n,ansl))
    
    print(ans)

        
